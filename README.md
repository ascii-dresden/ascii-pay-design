# ascii-pay-design

Dieses Skript fügt in das Design der ascii-pay EC-Karte den Namen und die Kennnummer ein. Außerdem generiert es den QR Code und fügt diesen ein. 

<img src="./images/examples/Max_Musterman_1234123412341234.png" width="49%"/> <img src="./images/examples/Eriphienela_de_Überlangnamigkeit_1234789312341234.png" width="49%"/>
Zwei Beispiel Karten: Rechts mit einem kurzen Namen und links mit der maximalen Namenslänge.

## Nutzung

```python main.py [path-to-csv] [-d optional-path-to-save-location]```

Beim ausführen des Skriptes muss eine Pfad zu einer csv-Datei angegeben werden, bei der sich in der ersten Salte die Namen und in der Zweiten Spalte die Nummern zu den Namen stehen. In **./data** befindet sich die Datei **test-data.csv**, welche ein Beispiel für eine funktionierende Struktur ist. Optional kann ein Pfad angegeben werden, an dem die generierten Bilder gespeichert werden. Wird kein Speicherpfad angegeben, werden die Bilder in **./images/results/** gesichert.
