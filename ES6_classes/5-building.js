export default class Building {
  constructor(sqft) {
    this._sqft = this.validateNumber(sqft, 'sqft');
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = this.validateNumber(value, 'sqft');
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }

  validateNumber(value, attribute) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new Error(`${attribute} must be a valid number.`);
    }
    return value;
  }
}
