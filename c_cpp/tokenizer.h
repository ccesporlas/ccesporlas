#include <string>

class Tokenizer
{
	public:
		Tokenizer(const std::string& s = "", char delimiter = " ");
		std::string getword();
		std::string getword(char delimiter);
		std::string getrest();

		void setDelimiter(char delimiter);
		char getDelimiter();
		void setString(const std::string& s);
		const std::string& getString();

	private:
		char _delimiter;
		std::string _str;
};