export default class HolbertonClass {
  constructor(size, location) {
    if (typeof value !== 'number' || isNaN(value) || value <= 0) {
      throw new Error(`${attribute} must be a valid positive number.`);
    }
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  set size(size) {
    this._size = size;
  }

  get location() {
    return this._location;
  }

  set location(location) {
    this._location = location;
  }

  valueOf = () => this._size;

  toString = () => this._location;
}
