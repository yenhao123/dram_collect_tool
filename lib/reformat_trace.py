from pathlib import Path
import pandas as pd
def split_file(in_path, o_dir, lines_per_file=10000000):
    file_count = 1
    try:
        with open(in_path, 'r') as file:
            while True:
                lines = [next(file) for _ in range(lines_per_file)]
                if not lines:
                    break

                o_path = o_dir / f"part{file_count}"
                with open(o_path, 'w') as new_file:
                    new_file.writelines(lines)
                
                file_count += 1

    except StopIteration:
        # 當 next(file) 沒有更多行時，會引發 StopIteration
        pass
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":

    to_4_col = True
    is_split = True
    data_dir = Path("/tmp2/mem_trace/object_detection")
    # CSV to 4 column CSV
    if not to_4_col:
        raw_trace = data_dir / "trace.csv"
        with open(raw_trace, "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if i % 100000 == 0:
                    print(f"Tackle {i} lines")
                
                lines[i] = lines[i].replace(",ldlat=30", "/ldlat=30")
                split_comma_line = lines[i].split(",")
                if len(split_comma_line) != 4:
                    print(lines[i])
                    raise "Error"

        im_trace = data_dir / "trace_sub_im.csv"
        with open(im_trace, "w") as f:
            f.writelines(lines)

        print("Done CSV to 4 column CSV")
    
    # Split
    if not is_split:
        im_trace = data_dir / "trace_sub_im.csv"
        o_dir = data_dir / "trace_sub_im_part"
        if not o_dir.exists():
            o_dir.mkdir()
        split_file(in_path=im_trace, o_dir=o_dir)

    # Read 4 column CSV
    im_trace_dir = data_dir / "trace_sub_im_part"
    o_dir = data_dir / "output"
    if not o_dir.exists():
        o_dir.mkdir()
    for i, file in enumerate(im_trace_dir.iterdir()):
        df = pd.read_csv(file, names=["commend", "time", "access", "addr"])

        df = df[df["commend"] == "benchmark_app"].reset_index(drop=True)

        df["time"] = df["time"].str.replace(":", "")
        df["time"] = df["time"].astype("float")
        df = df.sort_values(by="time")

        df["access"] = df["access"].replace({"cpu/mem-stores/P:" : "write", "cpu/mem-loads/ldlat=30/P:" : "read"})

        df["addr"] = "0x" + df["addr"]

        out_trace = o_dir / f"trace{i}.stl"
        with open(out_trace, "w") as f:
            for i in range(len(df)): 
                line = f"{i}:\t{df['access'][i]}\t{df['addr'][i]}"
                f.write(line + "\n")
        
        print(f"{file} Done")
