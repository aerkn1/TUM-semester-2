import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const directory = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(directory, 'eoq-epq-interactive-tutorial.html');
const notePath = path.join(directory, 'topic-05-eoq-production-systems-batching.md');

function readHtml() {
  return fs.readFileSync(htmlPath, 'utf8');
}

function extractMarkedBlock(html, startMarker, endMarker) {
  const start = html.indexOf(startMarker);
  const end = html.indexOf(endMarker);
  assert.notEqual(start, -1, `Missing marker: ${startMarker}`);
  assert.notEqual(end, -1, `Missing marker: ${endMarker}`);
  return html.slice(start + startMarker.length, end);
}

function loadTutorialApi() {
  const html = readHtml();
  const context = { console };
  context.globalThis = context;
  vm.createContext(context);
  vm.runInContext(
    extractMarkedBlock(
      html,
      '/* CALCULATION_CORE_START */',
      '/* CALCULATION_CORE_END */',
    ),
    context,
  );
  vm.runInContext(
    extractMarkedBlock(
      html,
      '/* PRESET_DATA_START */',
      '/* PRESET_DATA_END */',
    ),
    context,
  );
  return {
    api: context.EOQ_EPQ_CALCULATIONS,
    presets: context.EOQ_EPQ_PRESETS,
    html,
  };
}

function assertClose(actual, expected, tolerance = 0.02) {
  assert.ok(
    Math.abs(actual - expected) <= tolerance,
    `Expected ${actual} to be within ${tolerance} of ${expected}`,
  );
}

test('free-practice EOQ reproduces the saved clarification prompt', () => {
  const { api } = loadTutorialApi();
  const result = api.basicEoq({ demand: 9600, setupCost: 80, holdingCost: 6 });

  assertClose(result.quantity, 505.9644, 0.0001);
  assertClose(result.ordersPerPeriod, 18.9737, 0.0001);
  assertClose(result.averageInventory, 252.9822, 0.0001);
  assertClose(result.totalCost, 3035.7866, 0.0001);
});

test('ABI workflow compares separate warehouses with pooled demand', () => {
  const { api } = loadTutorialApi();
  const result = api.warehousePooling({
    warehouseCount: 2,
    demandPerWarehouse: 50,
    setupCost: 50,
    holdingCost: 20,
  });

  assertClose(result.separate.quantityPerWarehouse, 15.8114);
  assertClose(result.separate.totalCost, 632.4555);
  assertClose(result.pooled.quantity, 22.3607);
  assertClose(result.pooled.totalCost, 447.2136);
  assertClose(result.savings, 185.2419);
  assertClose(result.savingsPercent, 29.2893);
});

test('Tek Pak separates EOQ quantity from deterministic reorder timing', () => {
  const { api } = loadTutorialApi();
  const eoq = api.basicEoq({ demand: 130, setupCost: 25, holdingCost: 0.65 });
  const timing = api.eoqTiming({
    demand: 130,
    initialInventory: 100,
    leadTime: 2,
    periodsPerYear: 52,
  });

  assertClose(eoq.quantity, 100);
  assertClose(timing.demandPerSubperiod, 2.5);
  assertClose(timing.reorderPoint, 5);
  assertClose(timing.firstOrderPlacement, 38);
  assert.equal(timing.orderImmediately, false);
});

test('Kerosene finite horizon checks both integer neighbors', () => {
  const { api } = loadTutorialApi();
  const result = api.finiteHorizonEoq({
    demand: 8000,
    setupCost: 10,
    holdingCost: 2,
    horizonPeriods: 5,
    periodsPerYear: 52,
  });

  assertClose(result.infinite.quantity, 282.8427);
  assertClose(result.continuousOrders, 2.7196);
  assert.equal(result.floorCandidate.orders, 2);
  assertClose(result.floorCandidate.cost, 592.6154);
  assert.equal(result.ceilCandidate.orders, 3);
  assertClose(result.ceilCandidate.cost, 568.4103);
  assert.equal(result.optimal.orders, 3);
  assertClose(result.optimal.quantity, 256.4103);
  assertClose(result.costIncreasePercent, 0.4812);
});

test('Battery EPQ reproduces batch, inventory, duration, and cost reduction', () => {
  const { api } = loadTutorialApi();
  const result = api.epq({
    demand: 12000,
    productionRate: 60000,
    setupCost: 500,
    holdingCost: 4,
    periodsPerYear: 52,
  });

  assertClose(result.quantity, 1936.4917);
  assertClose(result.maximumInventory, 1549.1933);
  assertClose(result.productionDurationSubperiods, 1.6783);
  assertClose(result.totalCost, 6196.7734);
  assertClose(result.eoqBenchmarkCost, 6928.2032);
  assertClose(result.costReduction, 731.4298);
  assertClose(result.costReductionPercent, 10.5573);
});

test('Router EPQ reproduces preparation and production timing', () => {
  const { api } = loadTutorialApi();
  const result = api.epq({
    demand: 10400,
    productionRate: 52000,
    setupCost: 750,
    holdingCost: 6,
    periodsPerYear: 52,
  });
  const timing = api.eoqTiming({
    demand: 10400,
    initialInventory: 1300,
    leadTime: 2,
    periodsPerYear: 52,
  });

  assertClose(result.quantity, 1802.7756);
  assertClose(result.maximumInventory, 1442.2205);
  assertClose(result.cycleDurationSubperiods, 9.0139);
  assertClose(result.productionDurationSubperiods, 1.8028);
  assertClose(result.nonProductionDurationSubperiods, 7.2111);
  assertClose(timing.reorderPoint, 400);
  assertClose(timing.firstOrderPlacement, 4.5);
  assertClose(timing.firstReplenishment, 6.5);
});

test('Shovel workflow infers demand and values the technology improvement', () => {
  const { api } = loadTutorialApi();
  const result = api.shovelTechnology({
    productionRatePerPeriod: 200,
    maximumInventory: 150,
    currentBatch: 300,
    improvementPercent: 50,
    setupCost: 350,
    holdingCost: 5,
    previousCost: 6000,
    periodsPerYear: 52,
  });

  assertClose(result.demandPerSubperiod, 100);
  assertClose(result.demandAnnual, 5200);
  assertClose(result.newProductionRatePerSubperiod, 300);
  assertClose(result.newProductionRateAnnual, 15600);
  assertClose(result.newEpq.quantity, 1044.9880);
  assertClose(result.newEpq.maximumInventory, 696.6587);
  assertClose(result.newEpq.totalCost, 3483.2934);
  assertClose(result.maximumInvestment, 2516.7066);
});

test('invalid inputs are rejected before producing misleading results', () => {
  const { api } = loadTutorialApi();

  assert.throws(
    () => api.basicEoq({ demand: 0, setupCost: 80, holdingCost: 6 }),
    /demand must be greater than zero/i,
  );
  assert.throws(
    () => api.epq({ demand: 100, productionRate: 100, setupCost: 10, holdingCost: 2 }),
    /production rate must be greater than demand/i,
  );
});

test('the page contains all tutorial regions and seven workflow presets', () => {
  const { html, presets } = loadTutorialApi();
  const requiredIds = [
    'model-router',
    'workflow-selector',
    'input-panel',
    'calculation-ladder',
    'inventory-chart',
    'cost-chart',
    'interpretation-panel',
    'self-test-status',
  ];
  const presetKeys = [
    'free-practice',
    'abi-warehouses',
    'tek-pak',
    'kerosene',
    'battery-cell',
    'router-factory',
    'shovel-factory',
  ];

  requiredIds.forEach((id) => assert.match(html, new RegExp(`id=["']${id}["']`)));
  assert.deepEqual(Object.keys(presets), presetKeys);
  presetKeys.forEach((key) => assert.match(html, new RegExp(`data-workflow=["']${key}["']`)));
});

test('the tutorial is standalone and exposes dynamic renderers', () => {
  const { html } = loadTutorialApi();

  assert.doesNotMatch(html, /<script[^>]+src=/i);
  assert.doesNotMatch(html, /<link[^>]+rel=["']stylesheet/i);
  assert.doesNotMatch(html, /https?:\/\//i);
  ['renderEoqSawtooth', 'renderEpqTriangle', 'renderCostBars', 'renderCandidateBars'].forEach(
    (name) => assert.match(html, new RegExp(`function\\s+${name}\\s*\\(`)),
  );
});

test('the complete embedded JavaScript parses successfully', () => {
  const html = readHtml();
  const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map((match) => match[1]);
  assert.equal(scripts.length, 1);
  assert.doesNotThrow(() => new vm.Script(scripts[0]));
});

test('the page includes accessibility and responsive safeguards', () => {
  const html = readHtml();
  assert.match(html, /aria-live=["']polite["']/);
  assert.match(html, /aria-pressed=/);
  assert.match(html, /role=["']img["']/);
  assert.match(html, /prefers-reduced-motion/);
  assert.match(html, /@media \(max-width: 620px\)/);
});

test('validation is connected to the specific invalid input', () => {
  const html = readHtml();
  assert.match(html, /function\s+showFieldError\s*\(/);
  assert.match(html, /setAttribute\(['"]aria-invalid['"]/);
  assert.match(html, /field-error/);
});

test('the Topic 05 note links to the interactive tutorial', () => {
  const note = fs.readFileSync(notePath, 'utf8');
  assert.match(note, /eoq-epq-interactive-tutorial\.html/);
});
