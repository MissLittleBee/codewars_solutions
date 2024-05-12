"""Kata - Classy Extentions

completed at: 2023-03-07 09:01:13
by: Barbora Hůlová

<h1>Classy Extensions</h1>
Classy Extensions, this kata is mainly aimed at the new JS ES6 Update introducing <em>extends</em> keyword. You will be preloaded with the Animal class, so you should only edit the Cat class.

<h3>Task</h3>
Your task is to complete the Cat class which Extends Animal and replace the speak method to return the cats name + meows.
e.g. <code>'Mr Whiskers meows.'</code>

The name attribute is passed with this.name (JS), @name (Ruby) or self.name (Python).

Reference: [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes), [Ruby](http://rubylearning.com/satishtalim/ruby_inheritance.html), [Python](https://docs.python.org/2/tutorial/classes.html#inheritance).

"""

from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
Animal = Cat
