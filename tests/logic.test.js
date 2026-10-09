import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {rank,filterCases,reviewMessage} from '../dist/logic.js';
const data=JSON.parse(fs.readFileSync(new URL('../dist/catalogue.json',import.meta.url)));
test('all 75 cases stay accessible in two groups',()=>{assert.equal(filterCases(data,data.weights).length,75);assert.equal(filterCases(data,data.weights,{scope:'Healthcare'}).length,44);assert.equal(filterCases(data,data.weights,{scope:'Other healthcare'}).length,31);assert.equal(data.cases.find(c=>c.id==='vet-admin').category,'Other healthcare');assert.equal(data.cases.find(c=>c.id==='drug').sector,'Life sciences');});
test('default shortlist, company search and source filter work',()=>{assert.deepEqual(rank(data,data.weights).slice(0,5).map(c=>c.id),['inbox','intake','policy','callqa','appointments']);assert.deepEqual(filterCases(data,data.weights,{query:'Hemominas'}).map(c=>c.id),['appointments']);assert.ok(filterCases(data,data.weights,{source:'microsoft'}).every(c=>data.examples.some(e=>e.source_id==='microsoft'&&e.case_ids.includes(c.id))));assert.equal(filterCases(data,data.weights,{scope:'Other healthcare',query:'Animal health'}).length,1);});
test('demo requires input and routes clinical words before booking',()=>{assert.equal(reviewMessage(''),null);assert.equal(reviewMessage('Please reschedule my appointment').category,'Booking request');assert.equal(reviewMessage('Invoice copy').queue,'Billing team');assert.equal(reviewMessage('Cancel my appointment because of chest pain').queue,'Qualified care team');});
