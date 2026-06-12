import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const directory = path.dirname(fileURLToPath(import.meta.url));
const note = fs.readFileSync(path.join(directory, 'topic-05-eoq-production-systems-batching.md'), 'utf8');

function count(pattern) {
  return [...note.matchAll(pattern)].length;
}

function close(actual, expected, tolerance = 0.02) {
  assert.ok(Math.abs(actual - expected) <= tolerance, `${actual} is not within ${tolerance} of ${expected}`);
}

function eoq(demand, setupCost, holdingCost) {
  const quantity = Math.sqrt((2 * setupCost * demand) / holdingCost);
  const holding = holdingCost * quantity / 2;
  const setup = setupCost * demand / quantity;
  return { quantity, holding, setup, total: holding + setup };
}

function epq(demand, productionRate, setupCost, holdingCost) {
  const quantity = Math.sqrt((2 * setupCost * demand) / holdingCost) * Math.sqrt(productionRate / (productionRate - demand));
  const maximumInventory = ((productionRate - demand) / productionRate) * quantity;
  const holding = holdingCost * maximumInventory / 2;
  const setup = setupCost * demand / quantity;
  return { quantity, maximumInventory, holding, setup, total: holding + setup };
}

test('all six worked examples use the full operational learning structure', () => {
  assert.equal(count(/^#### Operating Story$/gm), 6);
  assert.equal(count(/^#### Asset Dictionary$/gm), 6);
  assert.equal(count(/^#### Full Operational Workflow$/gm), 6);
  assert.equal(count(/^#### Managerial Decision$/gm), 6);
  assert.equal(count(/^#### Exam Trap$/gm), 6);
});

test('all six bakery variants are expanded as operational mini-workflows', () => {
  const headings = [
    'Basic EOQ: Supplier Delivery',
    'Initial Inventory: Flour Already In Storage',
    'Positive Lead Time: Supplier Travel Time',
    'Initial Inventory Plus Lead Time: First-Order Timing',
    'Finite Horizon: Temporary Bakery Event',
    'EPQ: Flour Produced While Baking Continues',
  ];
  headings.forEach((heading) => assert.match(note, new RegExp(`^### ${heading}$`, 'm')));
  assert.match(note, /^### Bakery Flow Comparison$/m);
});

test('all five practice tasks are retrieval cards with operational prompts', () => {
  assert.equal(count(/^### Practice Task [1-5]:/gm), 5);
  assert.equal(count(/\*\*Operating setting:\*\*/g), 5);
  assert.equal(count(/\*\*Asset mapping:\*\*/g), 5);
  assert.equal(count(/\*\*Your task:\*\*/g), 5);
  assert.equal(count(/\*\*Physical interpretation prompt:\*\*/g), 5);
  assert.equal(count(/\*\*Exam-trap check:\*\*/g), 5);
});

test('ABI calculations remain correct', () => {
  const perWarehouse = eoq(50, 50, 20);
  const pooled = eoq(100, 50, 20);
  close(perWarehouse.quantity, 15.8114);
  close(perWarehouse.total * 2, 632.4555);
  close(pooled.quantity, 22.3607);
  close(pooled.total, 447.2136);
  close((perWarehouse.total * 2) - pooled.total, 185.2419);
});

test('Tek Pak and Kerosene calculations remain correct', () => {
  const tekPak = eoq(130, 25, 0.65);
  close(tekPak.quantity, 100);
  close((130 / 52) * 2, 5);
  close((100 - 5) / (130 / 52), 38);

  const infinite = eoq(8000, 10, 2);
  const horizon = 5 / 52;
  const mHat = horizon * Math.sqrt((2 * 8000) / (2 * 10));
  const cost = (m) => 10 * m / horizon + 2 * 8000 * horizon / (2 * m);
  close(infinite.quantity, 282.8427);
  close(mHat, 2.7196);
  close(cost(2), 592.6154);
  close(cost(3), 568.4103);
  close(horizon * 8000 / 3, 256.4103);
});

test('Battery, Router, and Shovel EPQ calculations remain correct', () => {
  const battery = epq(12000, 60000, 500, 4);
  close(battery.quantity, 1936.4917);
  close(battery.maximumInventory, 1549.1933);
  close(battery.total, 6196.7734);

  const router = epq(10400, 52000, 750, 6);
  close(router.quantity, 1802.7756);
  close(router.maximumInventory, 1442.2205);
  close(router.quantity / 52000 * 52, 1.8028);
  close(router.quantity / 10400 * 52, 9.0139);

  const demandPerWeek = 200 * (1 - 150 / 300);
  const shovel = epq(demandPerWeek * 52, 300 * 52, 350, 5);
  close(demandPerWeek, 100);
  close(shovel.quantity, 1044.9880);
  close(shovel.maximumInventory, 696.6587);
  close(shovel.total, 3483.2934);
  close(6000 - shovel.total, 2516.7066);
});
