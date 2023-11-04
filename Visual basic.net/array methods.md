Sure, here's the information in a tabular format:

| Method                   | Description                                                                  | Example Usage                                                  |
|--------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------|
| `Clear(Array, Int32, Int32)`     | Sets a range of elements in the array to zero, false, or null.                | `Array.Clear(myArray, 2, 2)`                                   |
| `Copy(Array, Array, Int32)`      | Copies a range of elements from one Array to another at the specified indices.| `Array.Copy(sourceArray, destinationArray, 5)`                |
| `CopyTo(Array, Int32)`           | Copies all the elements of the current Array to the specified destination.   | `sourceArray.CopyTo(destinationArray, 0)`                      |
| `IndexOf(Array, Object)`         | Searches for the specified Object and returns its index in a one-dimensional array. | `Array.IndexOf(myArray, 3)`                               |
| `Reverse(Array)`                 | Reverses the sequence of elements in a one-dimensional array.                  | `Array.Reverse(myArray)`                                       |
| `Sort(Array)`                    | Sorts the elements in a one-dimensional Array.                               | `Array.Sort(myArray)`                                          |

clear method
```vb
Dim myArray As Integer() = {1, 2, 3, 4, 5}
Array.Clear(myArray, 2, 2)
' Now myArray is {1, 2, 0, 0, 5}

copy method
Dim sourceArray As Integer() = {1, 2, 3, 4, 5}
Dim destinationArray As Integer() = New Integer(4) {}
Array.Copy(sourceArray, destinationArray, 5)
' Now destinationArray is {1, 2, 3, 4, 5}

copyto method
Dim sourceArray As Integer() = {1, 2, 3, 4, 5}
Dim destinationArray As Integer() = New Integer(4) {}
sourceArray.CopyTo(destinationArray, 0)
' Now destinationArray is {1, 2, 3, 4, 5}

index method
Dim myArray As Integer() = {1, 2, 3, 4, 5}
Dim index As Integer = Array.IndexOf(myArray, 3)
' index is 2

reversed method
Dim myArray As Integer() = {1, 2, 3, 4, 5}
Array.Reverse(myArray)
' Now myArray is {5, 4, 3, 2, 1}

sort method
Dim myArray As Integer() = {5, 3, 1, 4, 2}
Array.Sort(myArray)
' Now myArray is {1, 2, 3, 4, 5}

```

String method

| Method                    | Description                                                                        |
|---------------------------|------------------------------------------------------------------------------------|
| `Length`                  | Returns the length of the string.                                                 |
| `Clone`                   | Creates a new string object with the same value as the original string.           |
| `CompareTo`               | Compares the current string with another string.                                  |
| `Concat`                  | Concatenates one or more instances of String.                                     |
| `Contains`                | Returns a value indicating whether a specified substring occurs within the string. |
| `Copy`                    | Creates a new String object with the same value as the original string.           |
| `EndsWith`                | Determines whether the end of the string matches a specified string.              |
| `Equals`                  | Determines whether two String objects have the same value.                        |
| `GetEnumerator`           | Returns an enumerator that iterates through the string.                           |
| `GetHashCode`             | Returns the hash code for the string.                                             |
| `GetType`                 | Gets the Type of the current instance.                                            |
| `GetTypeCode`             | Gets the TypeCode for the current instance.                                       |
| `IndexOf`                 | Reports the zero-based index of the first occurrence of the specified string.      |
| `Insert`                  | Returns a new string in which a specified string is inserted at a specified index position. |
| `Intern`                  | Retrieves the system's reference to the specified string.                         |
| `IsNormalized`            | Determines whether the string is in Unicode normalization form C.                 |
| `LastIndexOf`             | Reports the zero-based index position of the last occurrence of a specified string within this instance. |
| `Normalize`               | Returns the Unicode normalization form of the string.                              |
| `Remove`                  | Returns a new string in which all occurrences of a specified string are removed.   |
| `Replace`                 | Returns a new string in which all occurrences of a specified string are replaced with another specified string. |
| `Split`                   | Returns a string array that contains the substrings in this string that are delimited by elements of a specified string array. |
| `StartsWith`              | Determines whether the beginning of this string instance matches a specified string. |
| `Substring`               | Retrieves a substring from this instance.                                          |
| `ToCharArray`             | Copies the characters in this instance to a character array.                       |
| `ToLower`                 | Returns a copy of this string converted to lowercase.                              |
| `ToLowerInvariant`        | Returns a copy of this String object converted to lowercase using the casing rules of the invariant culture. |
| `ToString`                | Returns the string itself.                                                         |
| `ToUpper`                 | Returns a copy of this string converted to uppercase.                              |
| `ToUpperInvariant`        | Returns a copy of this String object converted to uppercase using the casing rules of the invariant culture. |
| `Trim`                    | Removes all leading and trailing white-space characters from the current string.  |
| `TrimEnd`                 | Removes all trailing occurrences of a set of characters specified in an array from the current string. |
| `TrimStart`               | Removes all leading occurrences of a set of characters specified in an array from the current string. |
| `CopyTo`                  | Copies a specified number of characters from a specified position of the String to a specified position in an array of Unicode characters. |
| `ToCharArray`             | Returns an array of characters in the string.                                      |
| `ToCharArray(Int32, Int32)` | Copies characters from a specified position in this instance to a Unicode character array. |
| `Equals(Object)`          | Determines whether the specified Object is equal to the current Object.           |
| `Compare`                 | Compares two specified String objects and returns an integer that indicates their relative position in the sort order. |
| `CompareOrdinal`          | Compares two specified String objects by evaluating the numeric values of the corresponding characters in each string. |

code samples
```vb
' Declare a sample string
Dim myString As String = "Hello, World!"

' Length
Dim length As Integer = myString.Length

' CompareTo
Dim compareResult As Integer = String.Compare(myString, "Hello, Universe!")

' Concat
Dim concatenatedString As String = String.Concat(myString, " How are you?")

' Contains
Dim containsResult As Boolean = myString.Contains("World")

' EndsWith
Dim endsWithResult As Boolean = myString.EndsWith("!")

' IndexOf
Dim index As Integer = myString.IndexOf("W")

' Insert
Dim insertedString As String = myString.Insert(5, " Beautiful")

' Remove
Dim removedString As String = myString.Remove(5, 7)

' Replace
Dim replacedString As String = myString.Replace("Hello", "Hi")

' Split
Dim splitString() As String = myString.Split(","c)

' Substring
Dim substring As String = myString.Substring(7)

' ToLower
Dim lowerString As String = myString.ToLower()

' ToUpper
Dim upperString As String = myString.ToUpper()

' Trim
Dim trimmedString As String = myString.Trim()
```


Dictionary method

| Method                     | Description                                                          |
|----------------------------|----------------------------------------------------------------------|
| `Add`                      | Adds an element with the specified key and value into the dictionary. |
| `Clear`                    | Removes all keys and values from the dictionary.                      |
| `ContainsKey`              | Determines whether the dictionary contains the specified key.         |
| `ContainsValue`            | Determines whether the dictionary contains a specific value.          |
| `GetEnumerator`            | Returns an enumerator that iterates through the dictionary.            |
| `Remove`                   | Removes the element with the specified key from the dictionary.       |
| `TryGetValue`              | Gets the value associated with the specified key.                     |
| `Item` Property            | Gets or sets the value associated with the specified key.             |
| `Keys` Property            | Gets a collection containing the keys in the dictionary.              |
| `Values` Property          | Gets a collection containing the values in the dictionary.           |
| `Count` Property           | Gets the number of key/value pairs contained in the dictionary.       |

code samples
```vb
' Declare a sample dictionary
Dim dict As New Dictionary(Of String, String)()
dict.Add("key1", "value1")
dict.Add("key2", "value2")
dict.Add("key3", "value3")

' Item Property
Dim value As String = dict("key2")

' Keys Property
Dim keys As Dictionary(Of String, String).KeyCollection = dict.Keys

' Values Property
Dim values As Dictionary(Of String, String).ValueCollection = dict.Values

' Count Property
Dim count As Integer = dict.Count

' ContainsKey
Dim containsKeyResult As Boolean = dict.ContainsKey("key3")

' ContainsValue
Dim containsValueResult As Boolean = dict.ContainsValue("value2")

' Remove
Dim removeResult As Boolean = dict.Remove("key1")

' TryGetValue
Dim tryGetValueResult As Boolean = dict.TryGetValue("key2", value)

' Clear
dict.Clear()

```

Try Catch Exceptions

| Exception                  | Description                                                                      |
|----------------------------|----------------------------------------------------------------------------------|
| `AccessViolationException` | Thrown when there is an attempt to read or write protected memory.               |
| `ArgumentException`        | Thrown when one of the arguments provided to a method is not valid.              |
| `ArgumentNullException`     | Thrown when a method that does not allow null arguments is provided with a null argument. |
| `ArgumentOutOfRangeException` | Thrown when the value of an argument is outside the allowable range of values as defined by the called method. |
| `ArithmeticException`      | The base class for exceptions that occur during arithmetic operations.           |
| `ArrayTypeMismatchException` | Thrown when an attempt is made to store an object of the wrong type within an array. |
| `DivideByZeroException`    | Thrown when there is an attempt to divide an integral or decimal value by zero.   |
| `FormatException`          | Thrown when the format of an argument is invalid.                                |
| `IndexOutOfRangeException` | Thrown when an attempt is made to access an element of an array with an index that is outside its bounds. |
| `InvalidCastException`     | Thrown when there is an attempt to convert a value to a different data type, but the conversion cannot be performed. |
| `InvalidOperationException`   | Thrown when a method call is invalid for the object's current state.             |
| `InvalidProgramException`  | Thrown when a program contains invalid Microsoft intermediate language (MSIL) or metadata. |
| `KeyNotFoundException`     | Thrown when the specified key for accessing an element in a collection does not exist. |
| `NotFiniteNumberException` | Thrown when a floating-point value is positive infinity, negative infinity, or Not-a-Number (NaN). |
| `NotImplementedException` | Thrown when a method or operation is not implemented.                            |
| `NotSupportedException`   | Thrown when a method or operation is not supported.                              |
| `NullReferenceException`  | Thrown when an attempt is made to access a member on a null object.              |
| `OutOfMemoryException`    | Thrown when the system is unable to allocate the necessary memory.              |
| `OverflowException`       | Thrown when an arithmetic, casting, or conversion operation results in an overflow. |
| `StackOverflowException`  | Thrown when the execution stack overflows because it contains too many nested method calls. |

use list to declare an array of infinity
```vb
 Sub main()
     Dim student As New List(Of String)

     student.Add("precious")
     student.Add("Blessing")
     cl(student(0))

     Console.ReadLine()

 End Sub

' Indefinite argument
Sub addmore(ParamArray numbers As Integer())
    Dim sum As Integer = 0
    For Each value In numbers
        sum += value
    Next
    cl(sum)
End Sub
```