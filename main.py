from Bing import Bing

def main():
	b = Bing("oliver@spryn.me", "KhzGeDtnd8ZbZ0XG8UnooEqhCbPGQD4nIUPBC0R4r0Q=")
	r = b.search("Chuck Testa")

	for row in r:
		print row.Title

if __name__ == "__main__": main()
