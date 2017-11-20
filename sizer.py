import math, argparse

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


def main():
  parser = argparse.ArgumentParser(
      description="Convert bytes to human readable representations")
  parser.add_argument("bytes", metavar="B", type=int, help="The size in bytes")
  args = parser.parse_args()

  print convert_size(args.bytes)

if __name__ == "__main__":
  main()
