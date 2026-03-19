import json
import os
import subprocess

directory = r"c:\Users\ahdmo\Desktop\ML Portfolio"
nb_path = os.path.join(directory, "07-machine-translation", "machine-translation.ipynb")
exports_dir = os.path.join(directory, "07-machine-translation", "exports")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        source = "".join(cell.get("source", []))
        # Look for the exact phrasing where input_sequences or similar long outputs are printed
        if "input_sequences" in source and "print(" in source:
            new_source = []
            modified = False
            for line in cell.get("source", []):
                if "print(input_sequences" in line or "print(target_sequences" in line:
                    line = "# " + line.strip("\n") + "  # Output hidden for cleaner reading\n"
                    modified = True
                new_source.append(line)
            
            if modified:
                cell["source"] = new_source
                cell["outputs"] = []  # Clear large outputs
                
        # Just in case the cell outputs were directly returning input_sequences (i.e. just "input_sequences" on the last line)
        if "input_sequences" in source and not "print" in source:
             # Check if output is huge
             if len(str(cell.get("outputs", []))) > 1000:
                 cell["outputs"] = []

with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Cleaned long prints in notebook. Re-exporting...")
subprocess.run(["python", "-m", "jupyter", "nbconvert", "--to", "html", nb_path, "--output-dir", exports_dir, "--ClearMetadataPreprocessor.enabled=True"], check=True)
print("Done.")
