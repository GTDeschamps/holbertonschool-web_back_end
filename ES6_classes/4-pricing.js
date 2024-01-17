import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = this.validateNumber(amount, 'amount');
    this._currency = this.validateCurrency(currency, 'currency');
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = this.validateNumber(value, 'amount');
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = this.validateCurrency(value, 'currency');
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  validateNumber(value, attribute) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new Error(`${attribute} must be a valid number.`);
    }
    return value;
  }

  validateCurrency(value, attribute) {
    if (!(value instanceof Currency)) {
      throw new Error(`${attribute} must be an instance of Currency.`);
    }
    return value;
  }
}
