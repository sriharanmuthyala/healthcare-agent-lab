import json
import unittest
from pathlib import Path
from discovery import rank

class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.catalogue = json.loads((Path(__file__).parent / 'dist/catalogue.json').read_text())

    def test_default_shortlist_and_source_provenance(self):
        ranked = rank(self.catalogue)
        self.assertEqual([c['id'] for c in ranked[:5]], ['inbox', 'intake', 'policy', 'callqa', 'appointments'])
        self.assertEqual(len({c['id'] for c in ranked}), 75)
        self.assertTrue(all(0 <= c['weighted_score'] <= 100 for c in ranked))

    def test_every_source_entry_maps_to_existing_workflows(self):
        entries = self.catalogue['examples']
        self.assertEqual(len(entries), 168)
        self.assertEqual(len({e['id'] for e in entries}), 168)
        ids = {c['id'] for c in self.catalogue['cases']}
        self.assertTrue(all(e['case_ids'] and set(e['case_ids']) <= ids for e in entries))
        self.assertEqual(sum(e['source_id'] == 'google' for e in entries), 115)
        self.assertEqual(sum(e['source_id'] == 'microsoft' for e in entries), 52)

    def test_priority_changes_and_filtering(self):
        weights = {k: 0 for k in self.catalogue['weights']}
        weights['safety'] = 100
        self.assertEqual(rank(self.catalogue, weights=weights)[0]['weighted_score'], 100)
        self.assertTrue(all(c['risk'] == 'Low' for c in rank(self.catalogue, risk='Low')))
        self.assertIn('referrals', [c['id'] for c in rank(self.catalogue, query='referral')])

    def test_invalid_weights_and_missing_evidence_fail(self):
        with self.assertRaises(ValueError):
            rank(self.catalogue, weights={k: 0 for k in self.catalogue['weights']})
        self.catalogue['cases'][0]['source_id'] = 'missing'
        with self.assertRaises(ValueError):
            rank(self.catalogue)

if __name__ == '__main__':
    unittest.main()
