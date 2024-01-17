export default class Currency {
  constructor(code, name) {
    this._code = this.validateString(code, 'code');
    this._name = this.validateString(name, 'name');
  }

  get code() {
    return this._code;
  }

  set code(value) {
    this._code = this.validateString(value, 'code');
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this.validateString(value, 'name');
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
