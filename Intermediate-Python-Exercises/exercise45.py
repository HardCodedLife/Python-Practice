import csv

def exercise45(read_filename: str, write_filename: str):
    with open(read_filename, mode = "r", newline = "") as file:
        reader = csv.DictReader(file)
        with open(write_filename, mode = "w", newline = "") as w_file:
            sum = 0
            total = 0
            writer = csv.DictWriter(w_file, fieldnames = reader.fieldnames)
            writer.writeheader()
            for row in reader:
                writer.writerow(row)
                sum += int(row['Salary'])
                total += 1
            writer.writerow({"Name":"Average", "Salary":f"{sum/total:.1f}"})
if __name__ == "__main__":
    from pathlib import Path
    file_in = Path("data-45.csv")
    file_out = Path("output-45.csv")
    with open(file_in, mode = "w", newline="") as file:
        file.write(
"""Name,Salary
Alice,50000
Bob,60000
Charlie,70000"""
                )
    exercise45(file_in, file_out)
    
    import subprocess

    # Run cat and wait for it to finish
    subprocess.run(["cat", file_in])
    subprocess.run(["echo", "\n------"])
    subprocess.run(["cat", file_out])


    file_in.unlink(missing_ok=True)
    file_out.unlink(missing_ok=True)
