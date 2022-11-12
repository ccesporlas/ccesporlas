#ifndef _LIST_H_
#define _LIST_H_
#include "Node.h"


class List{
      public:
	     List() : elem(0) {}

             void addnode(Node n);
             void remove(int index);

	     void push_back(Content c);
	     void erase(int index);

	     Content at(index);
	     Node* at_p(int index);
             
	     Node* start();
             Node* next();
	     Node* begin();
	     Node* end();
             
	     Node getNode(int index);
	     void setNode(Node node);

      private:
              Node* startnode;
              Node* endnode;
              Node* nodenow;
	      int elem; 
              Node* lastnode;
              Node* prevnode;
}; 

#endif

