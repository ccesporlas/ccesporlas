#include "Node.h"
#include "List.h"
#include <iostream>


void List::addnode(Node n){
	if(!elem){
		startnode = &n;
		prevnode = startnode;
		elem++;
	}
	else {
		prevnode->setNextNode(&n);//set next node of previous node to current node
		lastnode = &n;
		prevnode = lastnode;
		nodenow = &n;
		lastnode = n.Next();
		elem++;
	}
}

void List::remove (int index){
	int countindex = 0;
	Node* current;
	Node* prevcurrent;

	if (index<=0 || index>elem || !elem){
		std::cerr<<"Out of bounds"<<"/n";
		return;
	}

	current = startnode;//set current node to first node
	for (countindex=1;countindex<index;countindex++){
		prevcurrent = current;//make the current node the previous node
		current = current->Next();
	}

	current = current->Next();
	prevcurrent->setNextNode(current);
	elem--;
}

Node* List::start(){
	return startnode;
}//to follow

Node* List::next(){
	if (nodenow->Next()){
		nodenow = nodenow->Next();
		return nodenow;
	}
	else{
		return 0;
	}
}//to follow

Node List::getNode(int index){

	if (index<=0 || index>elem || !elem){
		std::cerr<<"Out of bounds"<<"/n";
		return -11111;
	}

	Node* current;
	current = startnode;
	for (int countindex = 1; countindex!=index; countindex++){
		current = current->Next();
	}

	return *current;
}

void List::setNode(Node node){}//to follow


Content List::at(int index){

	Node* n;
	if (index<0 || index>elem || !elem){
		std::cerr<<"Out of bounds"<<"/n";
		return "ERROR";
	}
	n = startnode
	for (int count=0;count-1<index;count++){
		n = n->next();
	}

	return n->getContent();
}

Node* List::at_p(int index){
	Node* n;
	if (index<0 || index>elem || !elem){
		std::cerr<<"Out of bounds"<<"/n";
		 return 0;
	}
	n = startnode;
	if (int count=0;count<index-1;count++){
		n=n->next;
	}
	return n;

}

Node* List::begin(){
	return startnode;
}

Node* List::end(){
	return lastnode;
}

