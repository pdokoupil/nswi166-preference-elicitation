# Preference elicitation assignment template

## Setup instructions
1. Start by cloning this repository
2. Make sure you have Python3 installed (verified with Python 3.9.x but other, reasonably old versions of Python3 should be fine as well)
3. Make sure you have installed all required (see [requirements.txt](./requirements.txt)) Python modules (you can install them by running: `pip install -r requirements.txt`)
4. You can start the Flask server either as `flask --debug run` (from [src](./src/) folder) or using `python3 app.py`. Since Flask server will be running in debug mode, whenever you make changes to any Python script and save the file, the file will automatically get "reloaded" and changes will be reflected (so you do not have to restart the server manually).

## Assignment instructions and notes
1. You will be working with files inside [preference-elicitation](./src/plugins/preference-elicitation/) folder. You can modify [HTML files](./src/plugins/preference-elicitation/templates/), [.CSS and .JS files](./src/plugins/preference-elicitation/static/) and [plugin's Python script](./src/plugins/preference-elicitation/__init__.py) (or introduce arbitrary Python files for that plugin).
2. You can use arbitrary Python packages (add them to [requirements.txt](./requirements.txt))), except for full preference-elicitation solutions.
3. You can use arbitrary Javascript libraries (and their styles) as long as they can be imported using `<link>` or `<script src="...">` syntax, i.e. you SHOULD NOT (unfortunately, but there is a purpose for it in this specific case) use JS bundlers like npm or something similar that would require changing project structure or running additional servers.
4. Select a dataset (e.g. MovieLens, LastFM, etc.)
5. High-level goal is to prepare an HTML page (single page is enough) with some Javascript where you will present a set of questions/comparisons to be answered by the user (e.g. *How do you like these movies?* *Which of these movies do you like the most?* etc.). Then you can send the user's answers to the backend (implement `"/preference-elicitation"` endpoint, and/or additionally you can introduce arbitrary endpoints in [\_\_init\_\_.py](./src/plugins/preference-elicitation/__init__.py)), see `"/some-example"` endpoint for an inspiration). In the endpoint, you will process the data and implement a preference elicitation algorithm based on your specific assignment version. The endpoint should return a list of ratings for the given "user" (meaning a person who submitted the questions) and all items.
6. Follow other steps (if any) from your particular assignment version.
