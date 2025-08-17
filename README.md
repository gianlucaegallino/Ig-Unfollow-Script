# Auto-Unfollow (or Block) on Instagram 🚫📱

This script automates the process of unfollowing or blocking users on Instagram Web using **PyAutoGUI**.
It works with a list of usernames you provide and interacts with Instagram’s UI automatically.

⚠️ **Important**:

* Must use **Light Mode**
* Must use **English language** on Instagram

---

## Requirements 📦

* Python 3.13.7 🐍
* Dependencies listed in `requirements.txt` (install via `pip install -r requirements.txt`)
  * `pyautogui`
  * `numpy`

---

## Setup & Usage (English) 🇬🇧

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Get Your Non-Follower List 📋

1. Export your Instagram data (`Followers` + `Following`) as JSON.
2. Upload it to [followsback.com/instagram](https://followsback.com/instagram) to generate a **non-followers list**.
3. In your browser console, run:

   ```js
   let usernodes = document.querySelectorAll("td.break-all > span.font-bold");
   let myArray = Array.from(usernodes);
   let usernames = [];
   myArray.forEach(user => usernames.push(user.__reactProps$INSERTNAMEHERE.children));
   console.log(usernames)
   ```
4. Copy the array of usernames into the `NAME_LIST` variable in `script.py`.

### 3️⃣ Run the Script 🚀

```bash
python script.py
```

---

## Features & Customization 🛠️

### ✨ Features

* **Automated Unfollowing / Blocking**
  Choose between unfollowing or fully blocking accounts by toggling the `BLOCK` variable.

* **Order Control**
  Run in `OLDEST_TO_NEWEST` order, or newest first.

* **Runtime Estimation**
  Displays how long the script will take before starting.

* **Image Recognition**
  Uses screenshots in the `img/` folder to locate Instagram buttons (search, follow, block, etc).

* **Safety Checks**
  If an element is not found, the script safely stops instead of misclicking.

---

### 🔧 Customization

* **Unfollow vs Block**
  Set in `script.py`:

  ```python
  BLOCK = True   # block users
  BLOCK = False  # only unfollow users
  ```

* **Elimination Order**

  ```python
  OLDEST_TO_NEWEST = True   # oldest first
  OLDEST_TO_NEWEST = False  # newest first
  ```

* **Timing Tweaks**
  Adjust values like `BEGINNING_DELAY`, `FULL_LOAD`, `LOAD_WAIT` in `script.py` depending on your computer’s speed and internet connection.

* **Screenshots (`img/` folder)**
  Replace images if Instagram changes its UI. Filenames must match the ones referenced in the script (`search.PNG`, `block.PNG`, etc).

---

## Safety Notes ⚠️

* This script relies on pixel recognition, so it may misclick if Instagram changes its layout or if your screen resolution is unusual.
* Always test on a few accounts first before running on a large list.
* This tool is **not affiliated with Instagram** and may violate Instagram’s terms of service. Use responsibly.

---

# Auto-Unfollow (o Bloqueo) en Instagram 🚫📱

Este script automatiza el proceso de dejar de seguir o bloquear usuarios en **Instagram Web** usando **PyAutoGUI**.
Funciona con una lista de nombres de usuario que proporciones e interactúa automáticamente con la interfaz de Instagram.

⚠️ **Importante**:

* Debes usar **Modo Claro**
* El idioma de Instagram debe estar en **Inglés**

---

## Requisitos 📦

* Python 3.13.7 🐍
* Dependencias listadas en `requirements.txt` (instalar con `pip install -r requirements.txt`)

  * `pyautogui`
  * `numpy`

---

## Instalación y Uso (Español) 🇪🇸

### 1️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2️⃣ Obtener tu Lista de No-Seguidores 📋

1. Exporta tus datos de Instagram (`Seguidores` + `Seguidos`) en formato **JSON**.

2. Sube el archivo a [followsback.com/instagram](https://followsback.com/instagram) para generar una lista de **usuarios que no te siguen de vuelta**.

3. En la consola del navegador, ejecuta:

   ```js
   let usernodes = document.querySelectorAll("td.break-all > span.font-bold");
   let myArray = Array.from(usernodes);
   let usernames = [];
   myArray.forEach(user => usernames.push(user.__reactProps$INSERTNAMEHERE.children));
   console.log(usernames)
   ```

4. Copia el arreglo de nombres de usuario en la variable `NAME_LIST` dentro de `script.py`.

### 3️⃣ Ejecutar el Script 🚀

```bash
python script.py
```

---

## Funciones y Personalización 🛠️

### ✨ Funciones

* **Dejar de seguir o bloquear automáticamente**
  Elige entre dejar de seguir o bloquear cuentas cambiando la variable `BLOCK`.

* **Orden de eliminación**
  Ejecuta en orden de `OLDEST_TO_NEWEST` (más antiguos primero) o al revés.

* **Estimación de tiempo**
  Muestra cuánto tardará el script antes de empezar.

* **Reconocimiento por imágenes**
  Usa capturas en la carpeta `img/` para localizar botones de Instagram (buscar, seguir, bloquear, etc.).

* **Seguridad**
  Si un elemento no se encuentra, el script se detiene de forma segura en lugar de hacer clic en el lugar equivocado.

---

### 🔧 Personalización

* **Dejar de seguir vs Bloquear**
  Configura en `script.py`:

  ```python
  BLOCK = True   # bloquear usuarios
  BLOCK = False  # solo dejar de seguir
  ```

* **Orden de eliminación**

  ```python
  OLDEST_TO_NEWEST = True   # más antiguos primero
  OLDEST_TO_NEWEST = False  # más recientes primero
  ```

* **Ajustes de tiempo**
  Modifica valores como `BEGINNING_DELAY`, `FULL_LOAD`, `LOAD_WAIT` en `script.py` dependiendo de la velocidad de tu PC y tu conexión a internet.

* **Capturas de pantalla (`img/` folder)**
  Reemplaza las imágenes si Instagram cambia su interfaz. Los nombres de archivo deben coincidir con los que usa el script (`search.PNG`, `block.PNG`, etc.).

---

## Notas de Seguridad ⚠️

* Este script depende del reconocimiento de píxeles, por lo que puede fallar si Instagram cambia su diseño o si tu resolución de pantalla es distinta.
* Prueba primero con unas pocas cuentas antes de usarlo en una lista grande.
* Esta herramienta **no está afiliada a Instagram** y puede violar sus términos de servicio. Úsala con responsabilidad.


