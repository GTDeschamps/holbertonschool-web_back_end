export default class Airport {
  constructor(name, code) {
    this._name = this.validateString(name, 'name');
    this._code = this.validateString(code, 'code');
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this.validateString(value, 'name');
  }

  get code() {
    return this._code;
  }

  set code(value) {
    this._code = this.validateString(value, 'code');
  }

  toString() {
    return this._code;
  }

  validateString(value, attribute) {
    if (typeof value !== 'string') {
      throw new Error(`${attribute} must be a string.`);
    }
    return value;
  }
}
