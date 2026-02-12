If any changed file contains the string pattern /\beval\s*\(|\bexec\s*\(/i, then:
- Add a blocking Bug with title "Dangerous dynamic execution" and body:
  "Usage of eval/exec was found. Replace with safe alternatives or justify with a detailed comment and tests."
- Assign the Bug to the PR author.
- Apply label "security".
