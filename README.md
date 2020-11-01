# temp

Assumptions:

* Types include posts, or other schemas that are known to the data team.

* The transformation scripts are designed based on these schemas.

* The helper functions can be matched to the --type provided by the user. In this case, helper.py only transforms columns in posts.py, in the future, if a user types in 'blogs,py', the script will import 'hepler_blogs.py' for the corresponding functions.

* When truncating message columns, I deleted all puncutations first. The reason is that, most of the time, the punctuations don't contain meaningful signals for the end users -- data anaylsts or data scientists. However, this needs to be confirmed with the end users first before writing any scripts to transform the column.
