# Homework
#
# You will need to download 2 files for the homework.  First is the new w4_bank_accounts.txt (And then rename it to w4_bank_accounts.py) and the second is w4_homework_template.txt (and rename it to w4_homework.py)
#
# w4_bank_accounts.txt IS different than Week 3's bank_accounts.txt.
#
# Most of the code written for you so you can focus on the Regex and not the looping.  (If you run into import problems, check the from w4_bank_accounts line at the top.
#
# This file contains problems that you’ll need to find.  You can assume that you know the pattern of the file.  Meaning you can know what all the keys are, what type of data you should have.
# Your job...if you choose to accept it (actually you don’t have a choice, this is the homework J ) is to replace the locations where it says ‘FILL IN REGEX HERE’ with your regex patterns.
#
#     Validate all the names:  Names cannot have a number or symbols, but can have a hyphen, a period or spaces.
#     Validate the balance, can only be numbers
#     Validate the age:  Be logical on this one and must be >= 18
#     Validate a basic email:  Go get the one from the classwork!
#     Validate the state abbreviations.
#
# I’ve got 8 lines of errors in the file.   I’ve got 1 Email error, 3 age problems, one Balance problem, 1 firstname and 1 lastname.
#
# There are many different ways of getting your regex to work so as long as you pick out the problems then you did it!  A lot of why it’s different will come down to what is allowed and what isn’t by someone.

# These should be found #
email@domain.com                Valid email
firstname.lastname@domain.com   Email contains dot in the address field
email@subdomain.domain.com      Email contains dot with subdomain
firstname+lastname@domain.com   Plus sign is considered valid character
"email"@domain.com              Quotes around email is considered valid
1234567890@domain.com           Digits in address are valid
email@domain-one.com            Dash in domain name is valid
_______@domain.com              Underscore in the address field is valid
email@domain.name               .name is valid Top Level Domain name
email@domain.co.jp              Dot in Top Level Domain name also considered valid (use co.jp as example here)
firstname-lastname@domain.com   Dash in address field is valid

# We're going to skip these to keep things simplier, but should also be found as valid #
email@123.123.123.123           Domain is valid IP address
email@[123.123.123.123]         Square bracket around IP address is considered valid

# These should NOT be found #
plainaddress                    Missing at sign and domain
#@%^%#$@#$@#.com                Garbage
@domain.com                     Missing username
Joe Smith <email@domain.com>    Encoded html within email is invalid
email.domain.com                Missing @
email@domain@domain.com         Two @ sign
.email@domain.com               Leading dot in address is not allowed
email.@domain.com               Trailing dot in address is not allowed
email..email@domain.com         Multiple dots
あいうえお@domain.com             Unicode char as address
email@domain                    Missing top level domain (.com/.net/.org/etc)
email@-domain.com               Leading dash in front of domain is invalid
email@domain..com               Multiple dot in the domain portion is invalid


# We're going to skip these to keep things a bit simplier, but should also not be found #
email@domain.web                .web is not a valid top level domain
email@111.222.333.44444         Invalid IP format
email@domain.com (Joe Smith)    Text followed email is not allowed

# These should be found #
"  (404)   555-1212     "
"(404)555-1212  "
"  404-555-1212 "
"  404-5551212 "
" 4045551212"

# These should NOT be found #
"404 555-3355"
"404 555 3355"
