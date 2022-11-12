#include <iostream>

#include "List.h"
#include "Node.h"

void main()
{
	List l;

	l.push_back(0);
	std::cout << l.at(0); //0

	l.push_back(1);
	l.erase(0);
	std::cout << l.at(0); //1

	l.push_back(2);
	l.push_back(3);
	l.push_back(4);
	l.push_back(5);

	for (Node* i = l.begin(); i != l.end(); i = i->Next())
		std::cout << i->getContent(); //12345
}
	
