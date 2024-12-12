# Python Step by Step

Aufagbe : 1.1

## 1. Python-Installation
- Stelle sicher, dass Python auf deinem Rechner installiert ist.
- Überprüfen der Installation:

```bash
python3 --version
```
## wenn nicht vorhanden

Starte die die Windows Powershell und Instaliere WSL für Windows

```shell
wls --insatall
```
# Wichtige befehle

```python
 print("Hallo")

 # Ausgabe Hallo
```
Der Befehl print() gibt generell die Ausgabe in der Console aus was in den Klammern steht. Durch "" sage ich direkt aus was ausgeben werden soll. gebe ich einen wert hallo ohne "" an ist hallo in dem Fall einen Variable.

```python
hallo = "Hallo Welt!"

print(hallo)

# Ausgabe Hallo Welt!
```
hallo ist die Variable den (str String) definiert durch "" enthält ***Hallo Welt!***

weitere möglichkeiten wären:

 <table>
        <thead>
            <tr>
                <th>Variable</th>
                <th>Value</th>
                <th>Type</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>x</td>
                <td>"Hello World"</td>
                <td>str</td>
            </tr>
            <tr>
                <td>x</td>
                <td>20</td>
                <td>int</td>
            </tr>
            <tr>
                <td>x</td>
                <td>20.5</td>
                <td>float</td>
            </tr>
            <tr>
                <td>x</td>
                <td>1j</td>
                <td>complex</td>
            </tr>
            <tr>
                <td>x</td>
                <td>["apple", "banana", "cherry"]</td>
                <td>list</td>
            </tr>
            <tr>
                <td>x</td>
                <td>("apple", "banana", "cherry")</td>
                <td>tuple</td>
            </tr>
            <tr>
                <td>x</td>
                <td>range(6)</td>
                <td>range</td>
            </tr>
            <tr>
                <td>x</td>
                <td>{"name": "John", "age": 36}</td>
                <td>dict</td>
            </tr>
            <tr>
                <td>x</td>
                <td>{"apple", "banana", "cherry"}</td>
                <td>set</td>
            </tr>
            <tr>
                <td>x</td>
                <td>frozenset({"apple", "banana", "cherry"})</td>
                <td>frozenset</td>
            </tr>
            <tr>
                <td>x</td>
                <td>True</td>
                <td>bool</td>
            </tr>
            <tr>
                <td>x</td>
                <td>b"Hello"</td>
                <td>bytes</td>
            </tr>
            <tr>
                <td>x</td>
                <td>bytearray(5)</td>
                <td>bytearray</td>
            </tr>
            <tr>
                <td>x</td>
                <td>memoryview(bytes(5))</td>
                <td>memoryview</td>
            </tr>
            <tr>
                <td>x</td>
                <td>None</td>
                <td>NoneType</td>
            </tr>
        </tbody>
    </table>

[Weiter infos unter W3School](https://www.w3schools.com/python/python_datatypes.asp)