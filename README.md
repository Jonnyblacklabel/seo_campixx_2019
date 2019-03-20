# seo_campixx_2019

Meine Notebooks für die Vortrag auf der SEO Campixx 2019.

*Für eure tägliche Arbeit im Analytics- bzw. Data-Science-Umfeld empfehle ich euch **Anaconda** zu installieren. Damit bekommt ihr Python und Conda als Package Manager und Umgebung für virtuelle Environments. In diesem Projekt habe ich zum Erstellen des Environments **pipenv** genutzt.*

## Installation
*Achtung: die pipfile beinhaltet eine lokale binary. Diese ist für 64-Bit Windows.
[Quelle](https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-levenshtein)
Wenn ihr auf einem anderen Rechner unterwegs seid, kann `python-Levenstein` so nicht installiert werden.*
- Natürlich solltet ihr Python installiert haben (ab Version 3.7)
- Damit `pipenv` funktioniert, müsst ihr es mit `pip` installieren: `pip install pipenv --user`
- Environment erstellen und Packages installieren `pipenv install`
- node.js installieren z.B. von https://nodejs.org/en/ (für die nächsten Schritte nötig!)
- ipywidgets extension installieren `pipenv run jupyter labextension install @jupyter-widgets/jupyterlab-manager`
- Table of contents installieren `pipenv run jupyter labextension install @jupyterlab/toc`
- Qgrid Extension `pipenv run jupyter labextension install qgrid`
- RISE JS and CSS `pipenv run jupyter-nbextension install rise --py --sys-prefix`

## Jupyter starten
- Jupyter Lab `pipenv run jupyter lab`
- Jupyter Notebook `pipenv run jupyter notebook`
(oder die .bat Dateien nutzen)

## Notebooks ausprobieren
Die Notebooks nutzen Informationen aus der Environment-File (.env).
```
SISTRIX_KEY = [Sistrix Api Schlüssel]
CLIENT_ID = [Client ID des Google API Projekts]
CLIENT_SECRET = [Clientschlüssel des Google API Projekts]
```