#include "tokenizer.h"

Tokenizer::Tokenizer(const std::string& s = "", char delimiter = " ") :
	_str(s), _delimiter(delimiter)
{
}

void Tokenizer::setDelimiter(char delimiter)
{
	_delimiter = delimiter;
}

void Tokenizer::getdelimiter(delimiter)
{
	return _delimiter;
}

void Tokenizer::setString(const std::string& s)
{
	_str = s;
}

const std::string& Tokenizer::getString()
{
	return _str;
}