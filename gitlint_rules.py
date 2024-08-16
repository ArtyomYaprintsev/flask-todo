import re

from gitlint.git import StagedLocalGitCommit
from gitlint.rules import CommitRule, RuleViolation


class TitleRegexAndLengthRule(CommitRule):
    """Validate title regex and length.

    Custom gitlint rule that validates the commit title using regex and limits
    title length.
    """

    name = 'title-regex-and-length'
    id = 'UC1'

    def validate(
        self,
        commit: StagedLocalGitCommit,
    ) -> list[RuleViolation] | None:
        """Validate commit title."""
        # Regex playground: https://regex101.com/r/UoUFBq/1
        regex = r'^(:[a-z0-9_]+:\s)?([A-Z].{2,49})$'

        title = commit.message.title

        if re.fullmatch(regex, title):
            return None

        msg = (
            'Commit title is not valid. '
            'Commit title must start with an optional emoji and a capital '
            'letter. Max title length is 50 characters. '
            'Template: [:emoji:] Commit template. ',
            f'Got: {title}.'
        )

        return [RuleViolation(self.id, msg, title, line_nr=1)]
