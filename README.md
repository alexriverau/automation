# Lab: 19 - Automation

---

### Project: Automation
### Author: Alejandro Rivera

---

### Feature Tasks and Requirements

* Given a document potential-contacts, find and collect all email addresses and phone numbers.
* Phone numbers may be in various formats
  * (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
  * phone numbers with missing area code should presume 206
  * phone numbers should be stored in xxx-yyy-zzzz format.
* Once emails and phone numbers are found they should be stored in two separate documents. 
* The information should be sorted in ascending order. 
* Duplicate entries are not allowed.

phone_numbers.txt
```
123-456-7890
206-678-9012
234-567-8901
```
emails.txt
```
ana@foo.bar
bill_x@foo.bar
chris.schmidt@bar.baz
```

### Tests

The `phone_numbers.txt` and `emails.txt` files will be verified by an automated system. The naming/formatting requirements should match exactly.

