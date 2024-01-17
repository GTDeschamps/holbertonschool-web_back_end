# ES6 classes

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/817248fb77fb5c2cef3f.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240117%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240117T092907Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=13ddd608c495cf22f016d33bcfd9d92010ca4fdfbeb83968d3ad7d3a8408d6db" alt="" loading="lazy" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/AJdJxuoO8o3hwpybQaFSDQ" title="Classes" target="_blank">Classes</a></li>
<li><a href="/rltoken/jF42Fw5HNIPnFWKmDzVg1g" title="Metaprogramming" target="_blank">Metaprogramming</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/njFFGENoXPXVPrxCyuHqMg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>How to define a Class</li>
<li>How to add methods to a class</li>
<li>Why and how to add a static method to a class</li>
<li>How to extend a class from another</li>
<li>Metaprogramming and symbols</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x</li>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code>, <code>Visual Studio Code</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>js</code> extension</li>
<li>Your code will be tested using <code>Jest</code> and the command <code>npm run test</code></li>
<li>Your code will be verified against lint using ESLint</li>
<li>Your code needs to pass all the tests and lint. You can verify the entire project running <code>npm run full-test</code></li>
</ul>

<h2>Setup</h2>

<h3>Install NodeJS 12.11.x</h3>

<p>(in your home directory): </p>

<pre><code>curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
</code></pre>

<pre><code>$ nodejs -v
v12.11.1
$ npm -v
6.11.3
</code></pre>

<h3>Install Jest, Babel, and ESLint</h3>

<p>in your project directory: </p>

<ul>
<li>Install Jest using: <code>npm install --save-dev jest</code></li>
<li>Install Babel using: <code>npm install --save-dev babel-jest @babel/core @babel/preset-env</code></li>
<li>Install ESLint using: <code>npm install --save-dev eslint</code></li>
</ul>

<h2>Configuration files</h2>

<h3><code>package.json</code></h3>

<details>
<summary>
Click to show/hide file contents</summary>
<pre><code>
{
"scripts": {
"lint": "./node_modules/.bin/eslint",
"check-lint": "lint [0-9]*.js",
"dev": "npx babel-node",
"test": "jest",
"full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
},
"devDependencies": {
"@babel/core": "^7.6.0",
"@babel/preset-env": "^7.6.0",
"@babel/node": "^7.8.0",
"eslint": "^6.4.0",
"eslint-config-airbnb-base": "^14.0.0",
"eslint-plugin-import": "^2.18.2",
"eslint-plugin-jest": "^22.17.0",
"jest": "^24.9.0"
}
}
</code>
</pre>
</details>

<h3><code>babel.config.js</code></h3>

<details>
<summary>
Click to show/hide file contents</summary>
<pre><code>
module.exports = {
presets: [
[
'@babel/preset-env',
{
targets: {
node: 'current',
},
},
],
],
};
</code>
</pre>
</details>

<h3><code>.eslintrc.js</code></h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre><code>
module.exports = {
env: {
browser: false,
es6: true,
jest: true,
},
extends: [
'airbnb-base',
'plugin:jest/all',
],
globals: {
Atomics: 'readonly',
SharedArrayBuffer: 'readonly',
},
parserOptions: {
ecmaVersion: 2018,
sourceType: 'module',
},
plugins: ['jest'],
rules: {
'max-classes-per-file': 'off',
'no-underscore-dangle': 'off',
'no-console': 'off',
'no-shadow': 'off',
'no-restricted-syntax': [
'error',
'LabeledStatement',
'WithStatement',
],
},
overrides:[
{
files: ['*.js'],
excludedFiles: 'babel.config.js',
}
]
};
</code>
</pre>
</details>

<h3>and…</h3>

<p>Don’t forget to run <code>$ npm install</code> when you have the <code>package.json</code></p>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. You used to attend a place like this at some point
</h3>

Implement a class named <code>ClassRoom</code>:</p>

<ul>
<li>Prototype: <code>export default class ClassRoom</code></li>
<li>It should accept one attribute named <code>maxStudentsSize</code> (Number) and assigned to <code>_maxStudentsSize</code></li>
</ul>

<pre><code>bob@dylan:~$ cat 0-main.js
import ClassRoom from "./0-classroom.js";

const room = new ClassRoom(10);
console.log(room._maxStudentsSize)

bob@dylan:~$
bob@dylan:~$ npm run dev 0-main.js
10
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>0-classroom.js</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Let's make some classrooms
</h3>

Import the <code>ClassRoom</code> class from <code>0-classroom.js</code>. </p>

<p>Implement a function named <code>initializeRooms</code>. It should return an array of 3 <code>ClassRoom</code> objects with the sizes 19, 20, and 34 (in this order).</p>

<pre><code>bob@dylan:~$ cat 1-main.js
import initializeRooms from './1-make_classrooms.js';

console.log(initializeRooms());

bob@dylan:~$
bob@dylan:~$ npm run dev 1-main.js
[
ClassRoom { _maxStudentsSize: 19 },
ClassRoom { _maxStudentsSize: 20 },
ClassRoom { _maxStudentsSize: 34 }
]
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>1-make_classrooms.js</code></li>
</ul>
</div>

<h3 class="panel-title">
2. A Course, Getters, and Setters
</h3>

Implement a class named <code>HolbertonCourse</code>:</p>

<ul>
<li>Constructor attributes:

<ul>
<li><code>name</code> (String)</li>
<li><code>length</code> (Number)</li>
<li><code>students</code> (array of Strings)</li>
</ul></li>
<li>Make sure to verify the type of attributes during object creation</li>
<li>Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)</li>
<li>Implement a getter and setter for each attribute. </li>
</ul>

<pre><code>bob@dylan:~$ cat 2-main.js
import HolbertonCourse from "./2-hbtn_course.js";

const c1 = new HolbertonCourse("ES6", 1, ["Bob", "Jane"])
console.log(c1.name);
c1.name = "Python 101";
console.log(c1);

try {
c1.name = 12;
}
catch(err) {
console.log(err);
}

try {
const c2 = new HolbertonCourse("ES6", "1", ["Bob", "Jane"]);
}
catch(err) {
console.log(err);
}

bob@dylan:~$
bob@dylan:~$ npm run dev 2-main.js
ES6
HolbertonCourse {
_name: 'Python 101',
_length: 1,
_students: [ 'Bob', 'Jane' ]
}
TypeError: Name must be a string
...
TypeError: Length must be a number
...
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>2-hbtn_course.js</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Methods, static methods, computed methods names..... MONEY
</h3>

Implement a class named <code>Currency</code>:</p>

<ul>
<li>- Constructor attributes:

<ul>
<li><code>code</code> (String)</li>
<li><code>name</code> (String)</li>
</ul></li>
<li>Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)</li>
<li>Implement a getter and setter for each attribute. </li>
<li>Implement a method named <code>displayFullCurrency</code> that will return the attributes in the following format <code>name (code)</code>.</li>
</ul>

<pre><code>bob@dylan:~$ cat 3-main.js
import Currency from "./3-currency.js";

const dollar = new Currency('$', 'Dollars');
console.log(dollar.displayFullCurrency());

bob@dylan:~$
bob@dylan:~$ npm run dev 3-main.js
Dollars ($)
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>3-currency.js</code></li>
</ul>
</div>

<h3 class="panel-title">
4. Pricing
</h3>

Import the class <code>Currency</code> from <code>3-currency.js</code></p>

<p>Implement a class named <code>Pricing</code>:</p>

<ul>
<li>Constructor attributes:

<ul>
<li><code>amount</code> (Number)</li>
<li><code>currency</code> (Currency)</li>
</ul></li>
<li>Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)</li>
<li>Implement a getter and setter for each attribute. </li>
<li>Implement a method named <code>displayFullPrice</code> that returns the attributes in the following format <code>amount currency_name (currency_code)</code>.</li>
<li>Implement a static method named <code>convertPrice</code>. It should accept two arguments: <code>amount</code> (Number), <code>conversionRate</code> (Number). The function should return the amount multiplied by the conversion rate.</li>
</ul>

<pre><code>bob@dylan:~$ cat 4-main.js
import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

const p = new Pricing(100, new Currency("EUR", "Euro"))
console.log(p);
console.log(p.displayFullPrice());

bob@dylan:~$
bob@dylan:~$ npm run dev 4-main.js
Pricing {
_amount: 100,
_currency: Currency { _code: 'EUR', _name: 'Euro' }
}
100 Euro (EUR)
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>4-pricing.js</code></li>
</ul>
</div>

<h3 class="panel-title">
5. A Building
</h3>

Implement a class named <code>Building</code>:</p>

<ul>
<li>Constructor attributes:

<ul>
<li><code>sqft</code> (Number)</li>
</ul></li>
<li>Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)</li>
<li>Implement a getter for each attribute.</li>
<li>Consider this class as an abstract class. And make sure that any class that extends from it should implement a method named <code>evacuationWarningMessage</code>.

<ul>
<li>If a class that extends from it does not have a <code>evacuationWarningMessage</code> method, throw an error with the message <code>Class extending Building must override evacuationWarningMessage</code></li>
</ul></li>
</ul>

<pre><code>bob@dylan:~$ cat 5-main.js
import Building from './5-building.js';

const b = new Building(100);
console.log(b);

class TestBuilding extends Building {}

try {
new TestBuilding(200)
}
catch(err) {
console.log(err);
}

bob@dylan:~$
bob@dylan:~$ npm run dev 5-main.js
Building { _sqft: 100 }
Error: Class extending Building must override evacuationWarningMessage
...
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>5-building.js</code></li>
</ul>
</div>

<h3 class="panel-title">
6. Inheritance
</h3>

Import <code>Building</code> from <code>5-building.js</code>.</p>

<p>Implement a class named <code>SkyHighBuilding</code> that extends from <code>Building</code>:</p>

<ul>
<li>Constructor attributes:

<ul>
<li><code>sqft</code> (Number) (must be assigned to the parent class <code>Building</code>)</li>
<li><code>floors</code> (Number)</li>
</ul></li>
<li>Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)</li>
<li>Implement a getter for each attribute. </li>
<li>Override the method named <code>evacuationWarningMessage</code> and return the following string <code>Evacuate slowly the NUMBER_OF_FLOORS floors</code>.</li>
</ul>

<pre><code>bob@dylan:~$ cat 6-main.js
import SkyHighBuilding from './6-sky_high.js';

const building = new SkyHighBuilding(140, 60);
console.log(building.sqft);
console.log(building.floors);
console.log(building.evacuationWarningMessage());

bob@dylan:~$
bob@dylan:~$ npm run dev 6-main.js
140
60
Evacuate slowly the 60 floors
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>6-sky_high.js</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Airport
</h3>

Implement a class named <code>Airport</code>:</p>

<ul>
<li>Constructor attributes:

<ul>
<li><code>name</code> (String)</li>
<li><code>code</code> (String)</li>
</ul></li>
<li>Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)</li>
<li>The default string description of the class should return the airport <code>code</code> (example below).</li>
</ul>

<pre><code>bob@dylan:~$ cat 7-main.js
import Airport from "./7-airport.js";

const airportSF = new Airport('San Francisco Airport', 'SFO');
console.log(airportSF);
console.log(airportSF.toString());

bob@dylan:~$
bob@dylan:~$ npm run dev 7-main.js
Airport [SFO] { _name: 'San Francisco Airport', _code: 'SFO' }
[object SFO]
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>7-airport.js</code></li>
</ul>
</div>

<h3 class="panel-title">
8. Primitive - Holberton Class
</h3>

Implement a class named <code>HolbertonClass</code>:</p>

<ul>
<li>Constructor attributes:

<ul>
<li><code>size</code> (Number)</li>
<li><code>location</code> (String)</li>
</ul></li>
<li>Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)</li>
<li>When the class is cast into a <code>Number</code>, it should return the size. </li>
<li>When the class is cast into a <code>String</code>, it should return the location.</li>
</ul>

<pre><code>bob@dylan:~$ cat 8-main.js
import HolbertonClass from "./8-hbtn_class.js";

const hc = new HolbertonClass(12, "Mezzanine")
console.log(Number(hc));
console.log(String(hc));

bob@dylan:~$
bob@dylan:~$ npm run dev 8-main.js
12
Mezzanine
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>8-hbtn_class.js</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Hoisting
</h3>

Fix this code and make it work.</p>

<pre><code>const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

export class HolbertonClass {
constructor(year, location) {
this._year = year;
this._location = location;
}

get year() {
return this._year;
}

get location() {
return this._location;
}
}

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

export class StudentHolberton {
constructor(firstName, lastName) {
this._firstName = firstName;
this._lastName = lastName;
this._holbertonClass = holbertonClass;
}

get fullName() {
return `${this._firstName} ${this._lastName}`;
}

get holbertonClass() {
return this.holbertonClass;
}

get fullStudentDescription() {
return `${self._firstName} ${self._lastName} - ${self._holbertonClass.year} - ${self._holbertonClass.location}`;
}
}


export const listOfStudents = [student1, student2, student3, student4, student5];
</code></pre>

<p>Result:</p>

<pre><code>bob@dylan:~$ cat 9-main.js
import listOfStudents from "./9-hoisting.js";

console.log(listOfStudents);

const listPrinted = listOfStudents.map(
student => student.fullStudentDescription
);

console.log(listPrinted)

bob@dylan:~$
bob@dylan:~$ npm run dev 9-main.js
[
StudentHolberton {
_firstName: 'Guillaume',
_lastName: 'Salva',
_holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
},
StudentHolberton {
_firstName: 'John',
_lastName: 'Doe',
_holbertonClass: HolbertonClass { _year: 2020, _location: 'San Francisco' }
},
StudentHolberton {
_firstName: 'Albert',
_lastName: 'Clinton',
_holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
},
StudentHolberton {
_firstName: 'Donald',
_lastName: 'Bush',
_holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
},
StudentHolberton {
_firstName: 'Jason',
_lastName: 'Sandler',
_holbertonClass: HolbertonClass { _year: 2019, _location: 'San Francisco' }
}
]
[
'Guillaume Salva - 2020 - San Francisco',
'John Doe - 2020 - San Francisco',
'Albert Clinton - 2019 - San Francisco',
'Donald Bush - 2019 - San Francisco',
'Jason Sandler - 2019 - San Francisco'
]
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>9-hoisting.js</code></li>
</ul>
</div>

<h3 class="panel-title">
10. Vroom
</h3>

Implement a class named <code>Car</code>:</p>

<ul>
<li>Constructor attributes:

<ul>
<li><code>brand</code> (String)</li>
<li><code>motor</code> (String)</li>
<li><code>color</code> (String)</li>
</ul></li>
<li>Each attribute must be stored in an “underscore” attribute version (ex: <code>name</code> is stored in <code>_name</code>)</li>
<li>Add a method named <code>cloneCar</code>. This method should return a new object of the class.</li>
</ul>

<p>Hint: Symbols in ES6</p>

<pre><code>bob@dylan:~$ cat 10-main.js
import Car from "./10-car.js";

class TestCar extends Car {}

const tc1 = new TestCar("Nissan", "Turbo", "Pink");
const tc2 = tc1.cloneCar();

console.log(tc1);
console.log(tc1 instanceof TestCar);

console.log(tc2);
console.log(tc2 instanceof TestCar);

console.log(tc1 == tc2);

bob@dylan:~$
bob@dylan:~$ npm run dev 10-main.js
TestCar { _brand: 'Nissan', _motor: 'Turbo', _color: 'Pink' }
true
TestCar { _brand: undefined, _motor: undefined, _color: undefined }
true
false
bob@dylan:~$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>ES6_classes</code></li>
<li>File: <code>10-car.js</code></li>
</ul>
</div>

</details>
