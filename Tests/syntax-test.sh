#!/bin/bash
# This file should contain a lot of syntax examples to test highlighting with.

# Comment in column zero

foo bar # Comment after commands

"double quoted string"

'single quoted string'

string\ with\ escape\ sequences

"a \"quoted\" string"

<<END
here document
on multiple lines
END

<<ANOTHER
another heredoc
ANOTHER

<<-HERE
	a here-doc
	with initial indentation
		removed
HERE

<<<HERESTRING

simple_command

command --with arguments --and -- options

: # empty command

commands; and; more; commands

command --with line \
    continuation

command | with | pipeline

multiple && chained || commands

background_command &

(commands; in_a; subshell)

{ commands; in_a; list; }

(( 2 + 3 * 4 ))

let "2 + 3 * 4"

[ -n "$HOME" -a "$HOME" -eq "/home/me"  ]

[[ -n "$HOME" && "$HOME" == "/home/me" ]]

command --with file*/gl[ob]bing/pattern?

VARIABLE=assignment

$VARIABLE

${VARIABLE}

${VARIABLE:=default value}

${ARRAY[@]}

${ARRAY[2,-4]}

"string with $VARIABLE"

"string with ${VARIABLE}"

"string with ${VARIABLE:-value}"

'string without $VARIABLE'

'string without ${VARIABLE}'

'string without ${VARIABLE:-value}'

`command in backticks`

$(command in backtick-parens)

$(nested $(commands) in $(backtick-parens))

command --with $((2 + 3 * 4))


if [[ condition ]]; then
    statements
elif [[ another_condition ]]; then
    more statements
else
    other statements
fi

for (( i = 0; i < 10; i++ )); do
    statements
done

for w in words; do
    statements
done

select w in words; do
    statements
done

while [[ condition ]]; do
    statements
done

until [[ condition ]]; do
    statements
done

if [[ condition ]]; then; statements; elif [[ another_condition ]]; then; more statements; else; other statements; fi

for (( i = 0; i < 10; i++ )); do; statements; done

for w in words; do; statements; done

select w in words; do; statements; done

while [[ condition ]]; do; statements; done

until [[ condition ]]; do; statements; done

case word in
    pattern)
        do something
        ;;
    multiple|alternative|patterns)
        do something else
        ;;
    "quoted pattern")
        do something different
        ;;
    (yet|"even more"*|$patterns)
        do something entirely unrelated
        ;;
    *)
        do nothing
        ;;
esac

function_name () {
    statements
	# and comments
}

function function_name {
    statements
	# and comments
}

function function_name () {
	# comments and
    statements
}

function_name () { statements; }

function function_name { statements; }

function function_name () { statements; }
