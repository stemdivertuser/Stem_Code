# What is a JSON

JSON stands for **J**ava**S**script **O**bject **N**otation

It is an incredibly lightweight (small file size) way of storing and sending data

JSON files are easy for both humans and computers to understand

```yaml
{
"employees":[
    {"firstName":"John", "lastName":"Smith"},
    {"firstName":"Jane", "lastName":"Doe"},
    {"firstName":"Jennifer", "lastName":"Devonshire"}
]
}
```

Here you have a JSON Array (think of a list) of employees, inside this array are 3 JSON Objects.

`{"firstName":"John", "lastName":"Doe"}` is a JSON Object.

Inside each object is a bit of JSON Data `"firstName":"John"`, where `firstName` is the name of the data, and `John` is the value of the data.

You can then access this data really easily with `employees[0].firstName` which has the value `John`
