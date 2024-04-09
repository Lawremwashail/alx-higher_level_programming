#!/usr/bin/node
module.exports = class Square extends Rectangle require('./4-rectangle.js') {
	constructor (size) {
		super(size, size);
	}
};
