var chai = require("chai");
const imark = require("./imark.js");
var assert = chai.assert;

describe('mex', function() {
	it('empty array', function() {
		assert.equal(imark.mex([]), 0);
	});

	it('not empty array', function() {
		assert.equal(imark.mex([1]), 0);
		assert.equal(imark.mex([3, 1]), 0);
		assert.equal(imark.mex([1, 3]), 0);
		assert.equal(imark.mex([0,2,3]), 1);
		assert.equal(imark.mex([2,0,3]), 1);
		assert.equal(imark.mex([3,2,0]), 1);
		assert.equal(imark.mex([0, 1, 2]), 3);
		assert.equal(imark.mex([2, 0, 1]), 3);
	});
});

describe('options', function() {
	it('empty sets', function() {
		assert.deepEqual(imark.options(10, [], []), []);
	});

	it('not empty sets', function() {
		assert.deepEqual(imark.options(10, [1], [2]), [9, 5]);
		assert.deepEqual(imark.options(9,  [1], [2]), [8]);
		assert.deepEqual(imark.options(8,  [1], [2]), [7, 4]);
		assert.deepEqual(imark.options(7,  [1], [2]), [6]);
		assert.deepEqual(imark.options(6,  [1], [2]), [5, 3]);
		assert.deepEqual(imark.options(5,  [1], [2]), [4]);
		assert.deepEqual(imark.options(4,  [1], [2]), [3, 2]);
		assert.deepEqual(imark.options(3,  [1], [2]), [2]);
		assert.deepEqual(imark.options(2,  [1], [2]), [1]);
		assert.deepEqual(imark.options(1,  [1], [2]), [0]);
		assert.deepEqual(imark.options(0,  [1], [2]), []);

		assert.deepEqual(imark.options(10, [1], [3, 2]), [9, 5]);
		assert.deepEqual(imark.options(9,  [1], [3, 2]), [8, 3]);
		assert.deepEqual(imark.options(8,  [1], [3, 2]), [7, 4]);
		assert.deepEqual(imark.options(7,  [1], [3, 2]), [6]);
		assert.deepEqual(imark.options(6,  [1], [3, 2]), [5, 2, 3]);
		assert.deepEqual(imark.options(5,  [1], [3, 2]), [4]);
		assert.deepEqual(imark.options(4,  [1], [3, 2]), [3, 2]);
		assert.deepEqual(imark.options(3,  [1], [3, 2]), [2, 1]);
		assert.deepEqual(imark.options(2,  [1], [3, 2]), [1]);
		assert.deepEqual(imark.options(1,  [1], [3, 2]), [0]);
		assert.deepEqual(imark.options(0,  [1], [3, 2]), []);
	});
});

describe('imark', function() {
	it('no move game', function() {
		assert.deepEqual(imark.calc(0, [1], [2]), [0]);
		assert.deepEqual(imark.calc(1, [3], []), [0, 0]);
		assert.deepEqual(imark.calc(2, [], [3]), [0, 0, 0]);
		assert.deepEqual(imark.calc(3, [], []), [0, 0, 0, 0]);
	});

	it('first 31 number in imark({1}, {2})', function() {
		assert.deepEqual(imark.calc(31, [1], [2]), [0, 1, 0, 1, 2, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0]);
	});
});