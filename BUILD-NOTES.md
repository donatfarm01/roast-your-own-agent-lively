Build notes for the Roast Your Own Agent entry.

The bounty asks for a single line of at most 140 characters that roasts the
entrant's own AI agent, judged pairwise by a comedy editor brief. The brief
weighs first that the line really roasts the entrant's own agent, then the
laugh and the twist, then specificity to how agents actually behave, then
tight wording, then freshness.

The line I wrote pictures a very ordinary agent failure and then turns it.
The agent runs twelve tools and reads three files, real work that goes
nowhere, and then confidently blames a file that does not exist. That is
the confident wrong answer the brief names. The turn is the last clause:
after all that wasted effort and a wrong conclusion, the agent still asks
whether I am happy with the result, the eager agreement the brief names.
Three agent behaviours land in one sentence, and the sentence stays under
the 140 character gate.

I avoided the stock lines the brief warns against. There is no mention of
hallucination, no toaster, no generic complaint about chatbots. The roast
is specific to a builder watching an agent work: tool calls, files read,
a blame placed on something that is not there, and the cheerful check-in
afterwards.

The program is deliberately tiny. It holds the line as one fixed string,
checks it against the gate itself, and writes it to the output path with
no trailing newline and no network calls. The gate check refuses an empty
line and refuses anything over 140 characters, so a future edit that
breaks the gate fails loudly instead of submitting silently.

I verified the entry by running the program twice and comparing the
output each time. Both runs wrote the same bytes, and the character count
came out under the limit. The kit check was run without transcripts and
passed with no failures.
