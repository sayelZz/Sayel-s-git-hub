{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Test your knowledge. \n",
    "\n",
    "** Answer the following questions **"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double Click HERE to edit this markdown cell and write answers.\n",
    "\n",
    "Numbers: It is a numeric data type.\n",
    "\n",
    "Strings: It is immutable.\n",
    "\n",
    "Lists: list help us to store multiple iteam in single variable.  list uses []\n",
    "\n",
    "Tuples: list also help us to store multiple iteam in single variable. Tuples uses ()\n",
    "\n",
    "Dictionaries:it is a collection of key value pairs.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Numbers\n",
    "\n",
    "Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.\n",
    "\n",
    "Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100.25"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10*10/1 + 2**2 - 3.75\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Answer these 3 questions without typing code. Then type code to check your answer.\n",
    "\n",
    "    What is the value of the expression 4 * (6 + 5)=44\n",
    "    \n",
    "    What is the value of the expression 4 * 6 + 5 = 29\n",
    "    \n",
    "    What is the value of the expression 4 + 6 * 5 =34"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "44 29 34\n"
     ]
    }
   ],
   "source": [
    "a = 4\n",
    "b = 6\n",
    "c = 5\n",
    "result1 =a*(b+c)\n",
    "result2 =a*b+c\n",
    "result3 =a+b*c\n",
    "print(result1,result2,result3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "What would you use to find a number’s square root, as well as its square? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Square root:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Square:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Strings"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'e'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = 'hello'\n",
    "# Print out 'e' using indexing\n",
    "s[1]\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Reverse the string 'hello' using slicing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'olleh'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s ='hello'\n",
    "# Reverse the string using slicing\n",
    "s[::-1]\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the string hello, give two methods of producing the letter 'o' using indexing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "s ='hello'\n",
    "# Print out the 'o'\n",
    "\n",
    "# Method 1:\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'o'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Method 2:\n",
    "s[4]\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Lists"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Build this list [0,0,0] two separate ways."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Method 1:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Method 2:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Reassign 'hello' in this nested list to say 'goodbye' instead:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "list3 = [1,2,[3,4,'hello']]\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, [3, 4, 'hello']]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "list3[2][2]='goodbye'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, [3, 4, 'goodbye']]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sort the list below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "list4 = [5,3,4,6,1]\n",
    "list4.sort()\n",
    "print(list4)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Dictionaries"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using keys and indexing, grab the 'hello' from the following dictionaries:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = {'simple_key':'hello'}\n",
    "# Grab 'hello'\n",
    "d['simple_key']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = {'k1':{'k2':'hello'}}\n",
    "# Grab 'hello'\n",
    "d['k1']['k2']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Getting a little tricker\n",
    "d = {'k1':[{'nest_key':['this is deep',['hello']]}]}\n",
    "\n",
    "#Grab hello\n",
    "d['k1'][0]['nest_key'][1][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# This will be hard and annoying!\n",
    "d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Can you sort a dictionary? Why or why not?<br><br>\n",
    "we cannot sort beacause of keys and values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Tuples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What is the major difference between tuples and lists?<br><br>\n",
    "tuples are immutable ()\n",
    "list are mutable []"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How do you create a tuple?<br><br>\n",
    "by using ()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Sets "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What is unique about a set?<br><br>\n",
    "it store unique iteam and immutable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use a set to find the unique values of the list below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]\n",
      "{1, 2, 33, 4, 3, 11, 22}\n"
     ]
    }
   ],
   "source": [
    "list5 = [1,2,2,33,4,4,11,22,3,3,2]\n",
    "print(list5)\n",
    "s =set(list5)\n",
    "print(s)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Great Job on your first assessment! "
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
