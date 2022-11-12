#ifndef _NODE_H_
#define _NODE_H_

typedef int Content;

class Node
{
      Content content;
      Node* NextNode;

      public:
             Node() {}
             Node(Content c) : NextNode(0), content(c) {}
             void setNextNode(Node* N) {NextNode = N;}
             Node* Next() {return NextNode;}
             void setContent(Content c) {content = c;}
             Content getContent() {return content;}
};

#endif
