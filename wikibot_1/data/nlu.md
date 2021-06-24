## intent: input_greeting
- hey
- heyo
- hey hey
- hello
- hi
- hello there
- good morning
- good evening
- moin
- mornin
- afternoon
- hey there
- lets go
- sup
- yo
- yo yo
- yo yo yo
- hey dude
- goodmorning
- goodevening
- good afternoon

## intent: input_question_existence_1
- [is](existence) [serena williams]{"entity":"name"} in the system
- [do](existence) the statistics for [keren shlomo]{"entity":"name"} [exist](existence)
- [can](existence) you [find](existence) [philip bester]{"entity":"name"} in the database
- [will](existence) you please [find](existence) [novak djokovic]{"entity":"name"} in your registry
- [would](existence) [novak djokovic]{"entity":"name"} happen to [exist](existence) in your system
- [does](existence) [adam el mihdawy]{"entity":"name"} [appear](existence) in your files
- [does](existence) [adrian garcia]{"entity":"name"} [exist](existence) in your files

## lookup: name
data/lookups/name.txt

## intent: input_question_who_direct_primary_1
- [who](interrogative) is [serena williams](name)
- [who](interrogative) was [serena williams](name)
- [who](interrogative) is [novak djokovic](name)
- [who](interrogative) was [novak djokovic](name)
- [who](interrogative) is [sachia vickery](name)
- [who](interrogative) was [sachia vickery](name)
- [who](interrogative) is [thiago alves](name)
- [who](interrogative) was [thiago alves](name)
- [who](interrogative) is [keren shlomo](name)
- [who](interrogative) was [philip bester](name)
- [who](interrogative) is [adam el mihdawy](name)
- [who](interrogative) was [adrian garcia](name)
- [who](interrogative) is [albert montanes](name)
- [who](interrogative) was [marsel ilhan](name)
- [who](interrogative) is [wesley moodie](name)
- [who](interrogative) was [ze zhang](name)

## intent: input_question_who_indirect_1
- [who](interrogative) has the most [wins](keyword)
- [who](interrogative) has [won](keyword) the most [championships](keyword)

## intent: input_question_what_1
- [what](interrogative) is [serena williams](name) [date of birth](keyword)
- [what](interrogative) are [serena williams](name) [parents](person) names
- [what](interrogative) did [serena williams](name) do during [school](keyword)

## intent: input_question_where_1
- [where](interrogative) is [serena williams](name) house
- [where](interrogative) was [serena williams](name) [born](keyword)
- [where](interrogative) did [serena williams](name) [live](keyword)
- [where](interrogative) does [serena williams](name) [live](keyword)

## intent: input_question_when_1
- [when](interrogative) is [serena williams](name) [birthday](keyword)
- [when](interrogative) was [serena williams](name) [born](keyword)
- [when](interrogative) did [serena williams](name) [die](keyword)
- [when](interrogative) was [serena williams](name) [born](keyword)?
- [when](interrogative) was [serena williams](name) [born](keyword)
- [when](interrogative) was [serena williams](name) [born](keyword)?
- [when](interrogative) was [serena williams](name) [born](keyword)

## intent: input_question_why_1
- [why](interrogative) is [serena williams](name) [famous](keyword)
- [why](interrogative) was [serena williams](name) [playing](keyword)
- [why](interrogative) did [serena williams](name) [play](keyword)
- [why](interrogative) did [serena williams](name) [compete](keyword)

## intent: input_question_how_1
- [how](interrogative) is [serena williams](name) doing
- [how](interrogative) was [serena williams](name) early [life](keyword)
- [how](interrogative) did [serena williams](name) start [his](pronoun) [career](keyword)
