from typing import Optional
import csv
import json
import time
import functools
import logging
import sys

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start=time.perf_counter()
        
        res=func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info(f"{func.__name__} took {elapsed:6f} seconds")
        return res
    return wrapper
              
@timed
def clean_row(row:dict[str,str])->Optional[dict[str,str|int]]:
    name=row.get("name","").strip()
    age_str=row.get("age","").strip()
    if not name or not age_str:
        return None
    try:
        age=int(age_str)
    except ValueError:
        return None
    if age <= 0 or age > 120:
        return None
    
    return {"name":name,"age":age}

class Timer:
    def __enter__(self):
        self.start=time.time()
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        elapsed=time.time()-self.start
        logger.info(f"Took {elapsed:4f} seconds")
@timed
def main()->None:
    valid:list[dict[str,str|int]]=[]
    try:
        with open("people.csv","r",newline="",encoding="utf-8")as file:
            reader=csv.DictReader(file)
            for row in reader:
                cleaned=clean_row(row)
                if cleaned is not None:
                    valid.append(cleaned)
    except FileNotFoundError:
        logger.error("Error:people.csv not found in current directory")
        sys.exit(1)
    
    
    with open("people.json","w",encoding="utf-8") as file:
        json.dump(valid,file,indent=2)

if __name__=="__main__":
   
    with Timer():
        main()