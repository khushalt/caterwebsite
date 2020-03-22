/* eslint-disable */
// rename this file from _test_[name] to test_[name] to activate
// and remove above this line

QUnit.test("test: Website Homepage Item Groups", function (assert) {
	let done = assert.async();

	// number of asserts
	assert.expect(1);

	frappe.run_serially([
		// insert a new Website Homepage Item Groups
		() => frappe.tests.make('Website Homepage Item Groups', [
			// values to be set
			{key: 'value'}
		]),
		() => {
			assert.equal(cur_frm.doc.key, 'value');
		},
		() => done()
	]);

});
