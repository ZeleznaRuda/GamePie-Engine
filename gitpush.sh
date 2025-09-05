# 1️⃣ Přepni se do složky s repozitářem
cd /home/ruda/Dokumenty/Python/gamepie

# 2️⃣ Zkontroluj stav souborů
git status

# 3️⃣ Přidej všechny změny do commit
git add .

# 4️⃣ Vytvoř commit s popisem
git commit -m "add Messagebox and fix problems"

# 5️⃣ Stáhni vzdálené změny a proveď rebase
git pull origin main --rebase

# ⚠️ Pokud vzniknou konflikty:
#   a) uprav konfliktní soubory podle potřeby
#   b) pak proveď:
#      git add <soubor_který_jsi_upravoval>
#      git rebase --continue
#   c) opakuj, dokud rebase neskončí

# 6️⃣ Pushni změny na GitHub (použij token místo hesla)
git push https://github.com/ZeleznaRuda/GamePie-Engine main
