# Project blueprint — synthaudit

## Problem and scope
Researchers checking whether synthesis methods report key categories. The current repository scope is described by its README and implemented files.

## Architecture and contracts
Methods text → bounded text splitter → deterministic patterns → evidence snippets and completeness checklist. User content is untrusted data. Errors should be shown without disclosing private contents.

## Ground truth and review
Outputs must be checked against the input document, audio, or user-supplied evidence. No automated score proves scientific correctness or job suitability.

## Known limits
Keyword presence is not experimental correctness or chemical safety.

## Next milestone and acceptance
Fictional labelled examples with false-positive/false-negative analysis. The milestone is complete only when its implementation, meaningful tests, and measured results are committed.

## Release gate
Run automated tests, inspect realistic end-to-end output, record actual failures and limitations, and update the README before claiming the milestone.
