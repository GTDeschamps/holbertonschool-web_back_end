# Python - Variable Annotations

<p><img src="https://i.redd.it/y9y25tefi5401.png" alt="" loading="lazy" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/HkhGh45geTWVPwYQtwZxuw" title="Python 3 typing documentation" target="_blank">Python 3 typing documentation</a></li>
<li><a href="/rltoken/puu3jc5JT5rMI2B7EYdnXA" title="MyPy cheat sheet" target="_blank">MyPy cheat sheet</a></li>
</ul>

<h2>Learning Objectives</h2>

<h3>General</h3>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/u8rxH9rCLFQwUn_V3bV7aw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>Type annotations in Python 3</li>
<li>How you can use type annotations to specify function signatures and variable types</li>
<li>Duck typing</li>
<li>How to validate your code with <code>mypy</code></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5.)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. Basic annotations - add
</h3>

Write a type-annotated function <code>add</code> that takes a float <code>a</code> and a float <code>b</code> as arguments and returns their sum as a float. </p>

<pre><code>bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>0-add.py</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Basic annotations - concat
</h3>

Write a type-annotated function <code>concat</code> that takes a string <code>str1</code> and a string <code>str2</code> as arguments and returns a concatenated string</p>

<pre><code>bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)

bob@dylan:~$ ./1-main.py
True
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>1-concat.py</code></li>
</ul>
</div>

<h3 class="panel-title">
2. Basic annotations - floor
</h3>

Write a type-annotated function <code>floor</code> which takes a float <code>n</code> as argument and returns the floor of the float.</p>

<pre><code>bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

bob@dylan:~$ ./2-main.py
True
{'n': <class 'float'>, 'return': <class 'int'>}
floor(3.14) returns 3, which is a <class 'int'>
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>2-floor.py</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Basic annotations - to string
</h3>

Write a type-annotated function <code>to_str</code> that takes a float <code>n</code> as argument and returns the string representation of the float.</p>

<pre><code>bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))

bob@dylan:~$ ./3-main.py
True
{'n': <class 'float'>, 'return': <class 'str'>}
to_str(3.14) returns 3.14, which is a <class 'str'>
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>3-to_str.py</code></li>
</ul>
</div>

<h3 class="panel-title">
4. Define variables
</h3>

Define and annotate the following variables with the specified values:</p>

<ul>
<li><code>a</code>, an integer with a value of 1</li>
<li><code>pi</code>, a float with a value of 3.14</li>
<li><code>i_understand_annotations</code>, a boolean with a value of True</li>
<li><code>school</code>, a string with a value of “Holberton”</li>
</ul>

<pre><code>bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))

bob@dylan:~$ ./4-main.py
a is a <class 'int'> with a value of 1
pi is a <class 'float'> with a value of 3.14
i_understand_annotations is a <class 'bool'> with a value of True
school is a <class 'str'> with a value of Holberton
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>4-define_variables.py</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Complex types - list of floats
</h3>

Write a type-annotated function <code>sum_list</code> which takes a list <code>input_list</code> of floats as argument and returns their sum as a float.</p>

<pre><code>bob@dylan:~$ cat 5-main.py
#!/usr/bin/env python3

sum_list = __import__('5-sum_list').sum_list

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))

bob@dylan:~$ ./5-main.py
True
{'input_list': typing.List[float], 'return': <class 'float'>}
sum_list(floats) returns 6.470000000000001 which is a <class 'float'>
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>5-sum_list.py</code></li>
</ul>
</div>

<h3 class="panel-title">
6. Complex types - mixed list
</h3>

Write a type-annotated function <code>sum_mixed_list</code> which takes a list <code>mxd_lst</code> of integers and floats and returns their sum as a float.</p>

<pre><code>bob@dylan:~$ cat 6-main.py
#!/usr/bin/env python3

sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))

bob@dylan:~$ ./6-main.py
{'mxd_lst': typing.List[typing.Union[int, float]], 'return': <class 'float'>}
True
sum_mixed_list(mixed) returns 679.13 which is a <class 'float'>
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>6-sum_mixed_list.py</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Complex types - string and int/float to tuple
</h3>

Write a type-annotated function <code>to_kv</code> that takes a string <code>k</code> and an int OR float <code>v</code> as arguments and returns a tuple. The first element of the tuple is the string <code>k</code>. The second element is the square of the int/float <code>v</code> and should be annotated as a float.</p>

<pre><code>bob@dylan:~$ cat 7-main.py
#!/usr/bin/env python3

to_kv = __import__('7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))

bob@dylan:~$ ./7-main.py
{'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
('eggs', 9)
('school', 0.0004)
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>7-to_kv.py</code></li>
</ul>
</div>

<h3 class="panel-title">
8. Complex types - functions
</h3>

Write a type-annotated function <code>make_multiplier</code> that takes a float <code>multiplier</code> as argument and returns a function that multiplies a float by <code>multiplier</code>.</p>

<pre><code>bob@dylan:~$ cat 8-main.py
#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))

bob@dylan:~$ ./8-main.py
{'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}
4.928400000000001
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>8-make_multiplier.py</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Let's duck type an iterable object
</h3>

Annotate the below function’s parameters and return values with the appropriate types</p>

<pre><code>def element_length(lst):
return [(i, len(i)) for i in lst]
</code></pre>

<pre><code>bob@dylan:~$ cat 9-main.py
#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)

bob@dylan:~$ ./9-main.py
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>python_variable_annotations</code></li>
<li>File: <code>9-element_length.py</code></li>
</ul>
</div>

</details>
