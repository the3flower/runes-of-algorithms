module Greeting
    def hello
      "Hello from Greeting"
    end
end
  
class Person
    prepend Greeting
  
    def hello
      "Hello from Person"
    end
end
  
person = Person.new
puts person.hello