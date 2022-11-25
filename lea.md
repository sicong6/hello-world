# 学习

## Objective-C

Objective-C 是一种简单的计算机语言，设计为可以支持真正的面向对象编程。

Objective-Objective-C是C语言的严格超集－－任何C语言程序不经修改就可以直接通过Objective-C编译器，在Objective-C中使用C语言代码也是完全合法的。Objective-C被描述为盖在C语言上的薄薄一层，因为Objective-C的原意就是在C语言主体上加入面向对象的特性。

### OC 文件扩展名

| 扩展名 | 内容类型                                                     |
| ------ | ------------------------------------------------------------ |
| .h     | 头文件。头文件包含类，类型，函数和常数的声明。               |
| .m     | 源代码文件。这是典型的源代码文件扩展名，可以包含 Objective-C 和 C 代码。 |
| .mm    | 源代码文件。带有这种扩展名的源代码文件，除了可以包含Objective-C和C代码以外还可以包含C++代码。仅在你的Objective-C代码中确实需要使用C++类或者特性的时候才用这种扩展名。 |

当你需要在源代码中包含头文件的时候，你可以使用标准的 #include 编译选项，但是 Objective-C 提供了更好的方法。#import 选项和 #include 选项完全相同，只是它可以确保相同的文件只会被包含一次。

### 数据类型

基本数据类型：

| 类型                   | 字节数 | 格式化输出       |
| ---------------------- | ------ | ---------------- |
| char                   | 1      | %c               |
| int                    | 4      | %i, %x, %o       |
| unsigned int           | 4      | %i, %x, %o       |
| short int              | 2      | %hi, %hx, %ho    |
| unsigned short int     | 2      | %hi, %hx, %ho    |
| long int               | 8      | %li, %lx, %lo    |
| unsigned long int      | 8      | %lu, %lx, %lo    |
| long long int          | 8      | %lli, %llx, %llo |
| unsigned long long int | 8      | %llu, %llx, %llo |
| float                  | 4      | %f               |
| double                 | 8      | %f               |
| long double            | 16     | %lf              |

其他数据类型：

**id 类型** ：可以存放任何数据类型的对象，类似 Java 中的 Object 类，其被定义为指向对象的指针（本身就是指针），故定义比如 id instance = nil;id 类型是多态和动态绑定的基础。

**BOOL类型** ：布尔值为YES/NO或1/0。Java对应是true/false

**nil 和 Nil** ：nil 相当于 Java 中的 null，表示一个对象，这个对象的指针指向空。Nil 是定义一个指向空的类而不是对象。

**NSString (不可变字符串)** ：字符串是非常重要常用的，其基础用法包括创建、截取、遍历、比较、大小写转换、搜索等，语义跟基本类似 Java。

**NSMutableString (可变字符串)** ：创建对象的基本写法是 [[NSMutableString alloc]init]，* 号代表对象，[] 代表方法调用，只能通过类或者对象才能调用。[NSMutableString alloc] 类似 Java 中 new 得到一个对象，然后再调用 init 初始化方法。

```objective-c
NSString *str1 = @"ABC3456789"; //字符串
NSString *str2 = [str1 stringByAppendingString:@"wwww"]; //拼接成新的字符串
NSLog(@"str = %@", str2);
//遍历
for (int i = 0; i < [str2 length]; i++) {
    char temp = [str2 characterAtIndex:i];
    NSLog(@"字符串第 %d 位输出 %c", i, temp);
}
//比较
// sEqualToString方法 ：比较字符串是否完全相等，大小写不一样也无法完全匹配。
// hasPrefixe方法：逐一匹配字符串头部。haSuffix方法：匹配字符串的尾部
if ([str2 isEqualToString:str1]) {
    NSLog(@"相等");
}
if ([str2 hasPrefix:@"www"]) {
    NSLog(@"有该头部");
}
if ([str2 hasSuffix:@"www"]) {
    NSLog(@"有该尾部");
}
if ([str2 compare:str options:NSCaseInsensitiveSearch | NSNumericSearch] == NSOrderedSame) {
}
NSLog(@"比较结果：%d", [str2 caseInsensitiveCompare:str1]);
// 大小写转换
NSLog(@"str3转大写：%@",[str2 uppercaseString]);
NSLog(@"str3转小写：%@",[str2 lowercaseString]);
NSLog(@"str3首字母转大写：%@",[str2 capitalizedString]);
// 字符串截取
NSRange rang = NSMakeRange(2, 2);
NSLog(@"str3截取：%@",[str2 substringWithRange:rang]);
// 搜索
NSRange rang1 = [str2 rangeOfString:@"www"];
NSLog(@"location: %d,length: %d",rang1.location,rang1.length);
// 替换
NSString *str3 = [str2 stringByReplacingOccurrencesOfString:@" " withString:@"@"]; // 全部替换
NSString *str4 = [str2 stringByReplacingCharactersInRange:rang withString:@"met"]; // 局部替换

// 创建对象并初始化
NSMutableString *mStr = [[NSMutableString alloc]init];
// appendstring：向字符串尾部添加一个字符串。
// appendFormat：向字符串尾部添加多个类型的字符串，可以添加任意数量与类型的字符串。
[mStr appendString:@"hello world!"];
NSLog(@"字符串创建%@", mStr);
[mStr deleteCharactersInRange:[mStr rangeOfString:@"hello"]]; // 删除
NSLog(@"字符串删除%@", mStr);
[mStr insertString:@"love you" atIndex: mStr.length]; // 插入
NSLog(@"字符串插入%@", mStr);
```

**NSInteger、NSUInteger 和 NSNumber** ：NSInteger不是一个对象，而是基本数据类型中的typedef，NSUInteger是无符号的。 当需要使用int类型的变量时，推荐使用NSInteger，这样不需要考虑设备是32位或者64位。NSNumber是一个类，用于包装基本数据类型成为对象，可以理解为Java中的装箱，为一些集合只能存放对象使用，通过字面量方式非常方便将基本数据类型转成对应的对象。例如：

```objective-c
// 包装
NSNumber *intNumber = [[NSNumber alloc]initWithInt:43];
// 或者字面量方式
NSNumber *intNumber1 = @43;
// 还原基本数据类型，解包
NSLog(@"%d",[intNumber intValue]);
```



### 集合类

集合不能接受nil，nil是作为集合结束标识符。

#### 数组

**NSArray(不可变)** ：类似 Java 中的 ArrayList，可以存储不同类型的对象，一般情况下数组元素的类型是相同的，特点是有序、可重复。一维数组的基本操作：

```objective-c
//字面量创建方式
NSArray *arr2 = @[@"aaa",@"bbbbb"];
//工厂方法创建
NSArray *array = [[NSArray alloc] initWithObjects:@"1", @"2", nil];
//取最后一个元素
[array lastObject];
//取第一个元素
[array firstObject];
//数组是否包含某个元素
[array containsObject:@"1"];
//数组的大小
int count = (int) array.count;
//第一种方式遍历
for (int i = 0; i < count; i++) {
    NSString *_str = [array objectAtIndex:i];
}

// 字面量创建二维数组并访问
NSArray *arr2 = @[@[@11, @12, @13], @[@21, @22, @23], @[@31, @32, @33]];
// 字面量访问方式(推荐)
NSLog(@"arr2[2][2]:%@", arr2[2][2]);
// 数组对象函数访问
NSLog(@"arr2[2][2]:%@", [[arr2 objectAtIndex:2] objectAtIndex:2]);
```

**NSMutableArray(可变的)** ：派生于NSArray，理解为动态数组，提供增加、删除、插入、替换等语法。

```objective-c
//创建，当然还有其他方式
NSMutableArray *mutableArr = [NSMutableArray arrayWithObjects:@"one",@"two",@"three", nil];
//添加
[mutableArr addObject:@"hello"];
//替换
[mutableArr replaceObjectAtIndex:2 withObject:@"tihuan"];
//删除
[mutableArr removeObjectAtIndex:1];
//插入
[mutableArr insertObject:@"ios" atIndex:1];

// 多维数组创建方式：初始化作为列的数组，看做4列
NSMutableArray *columnArray = [[NSMutableArray alloc]initWithCapacity:4];
// 初始化2个一维数组，每个一维数组有4个元素，看做1行4列，2行加起来就是2行4列
NSMutableArray *rowArray1 = [[NSMutableArray alloc]initWithCapacity:4];
NSMutableArray *rowArray2 = [[NSMutableArray alloc]initWithCapacity:4];
// 每个行依次增加数组元素
// 第一行
[rowArray1 addObject:@"11"];
[rowArray1 addObject:@"12"];
[rowArray1 addObject:@"13"];
[rowArray1 addObject:@"14"];
// 第二行
[rowArray2 addObject:@"21"];
[rowArray2 addObject:@"22"];
[rowArray2 addObject:@"23"];
[rowArray2 addObject:@"24"];
// 分别打印数组
NSLog(@"myRowArray1: %@", rowArray1);
NSLog(@"myRowArray2: %@", rowArray2);
NSLog(@"myColumnArray: %@", columnArray);
```



#### 字典

类似于 Java 中的 HashMap，是一种映射型数据结果，存储键值对，有可变和不可变两种类型。

**NSDictionary** ：主要特点是不可变，如果集合初始化完成，将内容无法修改，无序。

```objective-c
//标准创建
NSDictionary *dict = [NSDictionary dictionaryWithObjectsAndKeys:@"cat",@"name1",@"dog",@"name2", nil];
//字面量创建
NSDictionary *dict1 = @{@"name1":@"cat",@"name2":@"dog"};
//第一种遍历
for (NSString *key in [dict1 allKeys]) {
    NSLog(@"key: %@,value: %@", key, dict1[key]);
}
//第二种遍历方式，通过遍历器
NSEnumerator *rator = [dict keyEnumerator];
NSString *temp;
while (temp = [rator nextObject]) {
    NSLog(@"%@", temp);
}
//获取元素
dict1[@"name"];
[dict1 objectForKey:@"name"];
//集合元素的个数
NSInteger count = dict1.count;
//沙盒文件存储和读取Plist
[dict5 writeToFile:@"路径" atomically:YES];
NSDictionary *dict7 = [NSDictionary dictionaryWithContentsOfFile:@"路径"];
```

**NSMutableDictionary** ：NSMutableDictionary 是 NSDictionary 的子类。NSMutableDictionary 是可变的，动态添加、更改、删除元素，因此不能使用字面量方式（@{}）来创建一个可变字典。如果是不可变字典，出现了同名的key，那么后面的 key 对应的值不会被保存，反之是可变字典，出现了同名的 key，那么后面的值会覆盖前面的值。

```objective-c
//创建
NSMutableDictionary *dict = [NSMutableDictionary dictionary];
//添加
[dict setObject:@"dog" forKey:@"name"];
[dict setValue:@"18" forKey:@"age"];
//会将传入字典中所有的键值对取出来添加到dict中
[dict setValuesForKeysWithDictionary:@{@"name1":@"dog"}];
//取元素
[dict objectForKey:@"name"];
dict[@"name"];
//删除
[dict removeAllObjects];
[dict removeObjectForKey:@"name"];
[dict removeObjectsForKeys:@[@"name", @"age"]];
//更新，如果利用setObject方法给已经存在的key赋值，新值会覆盖旧值
[dict setObject:@"20" forKey:@"age"];
dict[@"age"] = @"30";
```



#### 集合

**NSSet && NSMutableSet**  ：具有很好的存取和查找功能，与NSArray相比NSSet的元素没有索引，特点是无序，不可重复，类似Java中的HashSet，其中NSMutableSet提供计算交并集的方法。

NSSet存储元素的过程：NSSet添加一个对象；调用对象的Hash方法得到hashCode；对象在底层Hash表的位置；位置冲突类似Java的HashSet。

> 注：推荐使用字面量方式创建对象，可以缩短代码长度，增加可读性。但是在创建数组的时候要注意，如果含有 nil 就会抛异常，因为字面量实际上”语法糖“，效果等同于先创建一个数组，然后再把所有的对象添加进来，保证数组不添加 nil。



### 字符串

作为 C 语言的超集，Objective-C 支持 C 语言字符串方面的约定。也就是说，单个字符被单引号包括，字符串被双引号包括。然而，大多数 Objective-C 通常不使用 C 语言风格的字符串；大多数框架把字符串传递给 NSString 对象。NSString 类提供了字符串的类包装，包括了对保存任意长度字符串的内建内存管理机制，支持 Unicode，printf 风格的格式化工具，等等。

因为这种字符串使用的非常频繁，Objective-C 提供了一个助记符可以方便地从常量值创建 NSString 对象。使用这个助记符，就是在普通的双引号字符串前放置一个 @ 符号，如下面的例子所示：

```objective-c
NSString* myString = @"My String\n";  // 用于类和常数的“NS”前缀来自于 Cocoa 的来源，NeXTSTEP
NSString* anotherString = [NSString stringWithFormat:@"%d %s", 1, @"String"];
// 从一个C语言字符串创建Objective-C字符串
NSString*  fromCString = [NSString stringWithCString:"A C string" 
encoding:NSASCIIStringEncoding];
```

### 消息传递

Objective-C 最大的特色是承自 Smalltalk 的消息传递模型（message passing），此机制与C++式的主流风格差异甚大。Objective-C 里，与其说对象互相调用方法，不如说对象之间互相传递消息更为精确。

C++里，送一个消息给对象（或者说调用一个方法）的语法如下：

```c++
obj.method(argument);
```

Objective-C则写成：

```objective-c
[obj method: argument];
```

典型的 C++ 意义解读是"调用 car 类别的 fly 方法"。若 car 类别里头没有定义 fly 方法，那编译肯定不会通过。但是 Objective-C 里，我们应当解读为"发提交一个fly 的消息给car对象"，fly 是消息，而 car 是消息的接收者。car 收到消息后会决定如何回应这个消息，若 car 类别内定义有 fly 方法就运行方法内之代码，若 car 内不存在 fly 方法，则程序依旧可以通过编译，运行期则抛出异常，不会出错或崩溃。

此二种风格各有优劣。C++ 强制要求所有的方法都必须有对应的动作，且编译期绑定使得函数调用非常快速。缺点是仅能借由 virtual 关键字提供有限的动态绑定能力。

### 类

类是 Objective-C 用来封装数据，以及操作数据的行为的基础结构。对象就是类的运行期间实例，它包含了类声明的实例变量自己的内存拷贝，以及类成员的指针。Objective-C 的类规格说明包含了两个部分：定义（interface）与实现（implementation）。定义（interface）部分包含了类声明和实例变量的定义，以及类相关的方法。实现（implementation）部分包含了类方法的实际代码。

以下的代码展现了声明一个叫做 MyClass 类的语法，这个类继承自 NSObject 基础类。**类声明**总是由 @interface 编译选项开始，由 @end 编译选项结束。类名之后的（用冒号分隔的）是父类的名字。类的实例（或者成员）变量声明在被大括号包含的代码块中。实例变量块后面就是类声明的方法的列表。每个实例变量和方法声明都以分号结尾。类的定义文件遵循 C 语言之惯例以.h为后缀，实现文件以 .m 为后缀。

```objective-c
@interface MyObject : NSObject {
    int memberVar1; // 实体变量
    id  memberVar2;
}

+(return_type) class_method; // 类方法

-(return_type) instance_method1; // 实例方法
-(return_type) instance_method2: (int) p1;
-(return_type) instance_method3: (int) p1 andPar: (int) p2;
@end
```

方法前面的 +/- 号为方法类型标识符，代表函数的类型：加号 (+) 代表类方法，不需要实例就可以调用，与 C++ 的静态函数相似。减号 (-) 即是一般的实例方法。

```c++
class MyObject : public NSObject {  // 一份意义相近的 C++ 语法对照
protected:
    int memberVar1;  // 实体变量
    void * memberVar2;

  public:
    static return_type class_method(); // 类方法

    return_type instance_method1();    // 实例方法
    return_type instance_method2( int p1 );
    return_type instance_method3( int p1, int p2 );
}
```

Objective-C 定义一个新的方法时，名称内的冒号（:）代表参数传递，不同于C语言以数学函数的括号来传递参数。Objective-C方法使得参数可以夹杂于名称中间，不必全部附缀于方法名称的尾端，可以提高程序可读性。

```objective-c
- (void) setColorToRed: (float)red Green: (float)green Blue:(float)blue; /* 宣告方法*/
[myColor setColorToRed: 1.0 Green: 0.8 Blue: 0.2]; /* 呼叫方法*/
```

实现区块：包含了公开方法的实现，以及定义私有（private）变量及方法。 以关键字 @implementation 作为区块起头，@end 结尾。

```objective-c
@implementation MyObject {
  int memberVar3; //私有变量
}

+(return_type) class_method {
    .... //method implementation
}
-(return_type) instance_method1 {
     ....
}
-(return_type) instance_method2: (int) p1 {
    ....
}
-(return_type) instance_method3: (int) p1 andPar: (int) p2 {
    ....
}
@end
```

> 注：Interface 区块和 Implementation 区块都可以定义实体变量，两者的差别在于访问权限的不同。Interface 区块内的实体变量默认权限为 protected，宣告于 implementation 区块的实体变量则默认为 private。

创建对象：Objective-C 创建对象需通过 alloc 以及 init 两个消息。alloc 的作用是分配内存，init 则是初始化对象。 init 与 alloc 都是定义在 NSObject 里的方法，父对象收到这两个信息并做出正确回应后，新对象才创建完毕。若要自己定义初始化的过程，可以重写 init 方法，来添加额外的工作。（用途类似 C++ 的构造函数constructor）

```objective-c
MyObject * my = [[MyObject alloc] init];
People *p3 = [[People alloc] initWithNameAndAge:@"mingzi" andAge:12]; //调用自定义的构造方法
MyObject * my = [MyObject new];  // 在Objective-C 2.0里，若创建对象不需要参数，则可直接使用new。仅仅是语法上的精简，效果完全相同

// 重写初始化方法
- (instancetype)init
{
    self = [super init];
    if (self) {
        _peopleName = @"hello ios";
    }
    return self;
}
// 自定义初始化方法
- (instancetype)initWithNameAndAge:(NSString *)name andAge:(int)age
{
    self = [super init];
    if (self) {
        _peopleName = name;
        _peopleAge = age;
    }
    return self;
}
```

### 方法

Objective-C 中的类可以声明两种类型的方法：实例方法和类方法。实例方法就是一个方法，它在类的一个具体实例的范围内执行。也就是说，在你调用一个实例方法前，你必须首先创建类的一个实例。而类方法不需要你创建一个实例。

**方法声明** ：包括方法类型标识符，返回值类型，一个或多个方法标识关键字，参数类型和名信息。

**方法调用** ：就是传递消息给对应的对象。发送给对象的所有消息都会动态分发，这样有利于实现 Objective-C 类的多态行为。也就是说，如果子类定义了跟父类的具有相同标识符的方法，那么子类首先收到消息，然后可以有选择的把消息转发（也可以不转发）给他的父类。

**嵌套** ：为了避免声明过多的本地变量保存临时结果，Objective-C允许你使用嵌套消息。每个嵌套消息的返回值可以作为其他消息的参数或者目标。

```objective-c
[myArray insertObject:anObj atIndex:0];  // （调用方法）消息传递
[[myAppObject getArray] insertObject:[myAppObject getObjectToInsert] atIndex:0];  // 嵌套消息
```

除了传递消息给某个类的实例，也可以传递消息给类本身。当给类发消息，指定的方法必须被定义为类方法，而不是实例方法。类方法跟 C++ 类里面的静态成员有点像（但是不是完全相同的）。类方法的典型用途是用做创建新的类实例的工厂方法，或者是访问类相关的共享信息的途径。

下面演示一个类方法如何作为类的工厂方法。arrayWithCapacity 是 NSMutableArray 类的类方法，为类的新实例分配内容并初始化，然后返回给你。

```objective-c
NSMutableArray*   myArray = nil; // nil 基本上等同于 NULL
// 创建一个新的数组，并把它赋值给 myArray 变量
myArray = [NSMutableArray arrayWithCapacity:0];
```



### 属性

属性是用来代替声明存取方法的便捷方式。属性不会在你的类声明中创建一个新的实例变量。他们仅仅是定义方法访问已有的实例变量的速记方式而已。暴露实例变量的类，可以**使用属性记号代替 getter 和 setter 语法**。类还可以使用属性暴露一些“虚拟”的实例变量，他们是部分数据动态计算的结果，而不是确实保存在实例变量内的。

大多数存取方法都是用类似的方式实现的，属性避免了为类暴露的每个实例变量提供不同的 getter 和 setter 的需求。取而代之的是，你用属性声明指定你希望的行为，然后在编译期间合成基于声明的实际的 getter 和 setter 方法。

**属性声明** 应该放在类接口的方法声明那里。基本的定义使用 @property 编译选项，紧跟着类型信息和属性的名字。你还可以用定制选项对属性进行配置，这决定了存取方法的行为。

```objective-c
@interface Person : NSObject {
    @public
        NSString *name;
    @private
        int age;
}

@property(copy) NSString *name;
@property(readonly) int age;

-(id)initWithAge:(int)age;
@end
```

**属性的访问方法** 由 @synthesize 关键字来实现，它根据属性声明去自动地产生一对访问方法。另外，使用 @dynamic 关键字表明访问方法会由程序员手工提供。在OC中访问修饰符很少用到，主要是靠声明属性取值。属性有五个常用的特质修饰：

- assign：针对基本数据类型赋值操作。
- strong：定义一种”拥有关系“，属性设置新值时，先保留新值，并释放旧值，然后再将新值设置。
- weak：跟 strong 相反，属性所指的对象销毁时，属性值也会清空。
- copy：设置方法不保留新值，而是拷贝一份。
- nonatomic：非原子，非线程安全类型。

```objective-c
@implementation Person
@synthesize name;
@dynamic age;

-(id)initWithAge:(int)initAge
{
    age = initAge; // 注意：直接赋给成员变量，而非属性
    return self;
}

-(int)age
{
    return 29; // 注意：并非返回真正的年龄
}
@end
```

**属性的访问** 可以利用传统的消息表达式、点表达式或"valueForKey:"/"setValue:forKey:"方法。

```objective-c
Person *aPerson = [[Person alloc] initWithAge: 53];
aPerson.name = @"Steve"; // 注意：点表达式，等于[aPerson setName: @"Steve"];
NSLog(@"Access by message (%@), dot notation(%@), property name(%@) and direct instance variable access (%@)",
      [aPerson name], aPerson.name, [aPerson valueForKey:@"name"], aPerson->name);
```

为了利用点表达式来访问实例的属性，需要使用"self"关键字： （啥意思，没懂？？？？）

```objective-c
-(void) introduceMyselfWithProperties:(BOOL)useGetter
{
    NSLog(@"Hi, my name is %@.", (useGetter ? self.name : name)); // NOTE: getter vs. ivar access
}
```

类或协议的属性可以被动态的读取：（啥意思，没懂？？？？）

```objective-c
int i;
int propertyCount = 0;
objc_property_t *propertyList = class_copyPropertyList([aPerson class], &propertyCount);

for ( i=0; i < propertyCount; i++ ) {
    objc_property_t *thisProperty = propertyList + i;
    const char* propertyName = property_getName(*thisProperty);
    NSLog(@"Person has a property: '%s'", propertyName);
}
```



[内存管理](#jump)  
[跳转到 Table-1](#table1)        #



**Q&A：为什么NSString 、 NSArray、 NSDictionary的属性要用copy，集合的深浅拷贝是怎样的？** ？？？

copy 属性作用是为变量赋值的时候系统自动 copy 一份内存出来，修改新变量不会影响旧变量。在 Apple 规范中，NSString，NSArray，NSDictonary，推荐使用copy 属性，而其 NSMubtableString，NSMutableArray, NSMutableDictonary 属性则使用 strong 属性。

```objective-c
NSString *sourceString = [NSString stringWithFormat:@"hello ios"];
//不产生新的内存空间
NSString *copyStr = [sourceString copy];
//产生新的内存空间
NSMutableString *mutableStr = [sourceString mutableCopy];
NSLog(@"sourceString : %@   %p",sourceString,sourceString); // hello ios   1
NSLog(@"copyStr : %@    %p",copyStr,copyStr); // hello ios   1
NSLog(@"mutableStr : %@     %p",mutableStr,mutableStr); // hello ios   2
```

**结论** ：可变对象指向不可变对象会导致不可变对象的值被篡改，所以需要 copy 属性。用 @property 声明 NSString、NSArray、NSDictionary 经常使用 copy 关键字，是因为他们有对应的可变类型 NSMutableString、NSMutableArray、NSMutableDictionary，彼此之间可能进行赋值操作，为了不可变对象中的内容不会被无意间变动，应该在设置新属性值时拷贝一份。

- 浅拷贝：在 Java 中浅拷贝如果是基本数据，则拷贝的是基本数据的值；如果是对象，则拷贝的是内存地址，修改该对象会影响另外一个对象。在 OC 中是对指针的拷贝，拷贝后的指针和原本对象的指针指向同一块内存地址，故同样会相互影响。
- 深拷贝：OC 中不仅拷贝指针，而且拷贝指针指向的内容，指针指向不同的内存地址，故修改不会相互影响原本对象。

非集合类对象中：对 immutable 对象进行 copy 操作，是指针复制（浅拷贝），mutableCopy 操作时内容复制；对 mutable 对象进行 copy 和 mutableCopy 都是内容复制（深拷贝）。

#### 修饰属性的关键字

读写权限：

| 关键字名称        | 顾名思义 | 关键字描述           |
| ----------------- | -------- | -------------------- |
| readonly          | 只读     | 只具有get方法        |
| readwrite（默认） | 读写     | 同时具有set和get方法 |

原子性：

| 关键字名称     | 顾名思义 | 关键字描述                                   | 特点           |
| -------------- | -------- | -------------------------------------------- | -------------- |
| atomic（默认） | 原子的   | 生成setter方法的代码会被加上线程安全锁       | 安全、效率低   |
| nonatomic      | 非原子的 | 生成setter方法的代码**不会**被加上线程安全锁 | 效率高、不安全 |

内存管理：

| 关键字名称 | 顾名思义 | 所属时期           | 关键字描述                                                   | 修饰类型                                                     |
| ---------- | -------- | ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| retain     | 保留     | MRC                | 生成setter方法时，先判断新旧对象是否为同一个对象，如果不是，release（释放）旧的对象，retain（保留）新的对象 | 只能修饰NSObject对象，不能修饰基本的数据类型                 |
| assign     | 分配     | MRC                | 生成settet方法时，直接赋值                                   | 可以修饰基础数据类型和NSObject对象                           |
| strong     | 强的     | ARC                | 对对象强引用，每对这个属性引用一次，引用计数就会+1           | 只能修饰NSObject对象，不能修饰基本的数据类型，是id和对象的默认修饰符 |
| weak       | 弱的     | ARC                | 对对象弱引用，引用对象时，引用计数不变                       | 只能修饰NSObject对象，不能修饰基本的数据类型，防止循环引用，delegate一般都用weak修饰 |
| copy       | 复制     | 不属于某个特定时期 | 用于对象的拷贝                                               | 只能修饰NSObject对象，不能修饰基本的数据类型，多用于NSString类型 |

> 浅拷贝：拷贝指向某一内存的指针，但是在内存中并没有开辟一块新的空间。此时retainCount+1，这个+1是指原对象的引用计数+1。
>
> 深拷贝：拷贝一个完整的对象，且在内存中开辟了一块新的空间。此时原对象引用计数不变，新对象引用计数+1

> 对于不可变对象，使用copy是浅拷贝，使用mutableCopy是深拷贝
>
> 对于可变对象，使用copy与mutableCopy都是深拷贝



### 继承

同 Java 一样只能单继承，只允许最多有一个直接父类。例如：定义一个父类 Computer 和子类 MacBook。注意方法重写类似 Java，子类要重写父类方法不需要重新声明重写方法，在实现部分直接重写目标方法即可。如果需要子类调用父类的方法，可以通过 super 关键字调用。

```objective-c
//Computer.h文件
#import <Foundation/Foundation.h>
@interface Computer : NSObject
@property(nonatomic,strong)NSString *name;
-(void)calculate;
@end

//  Computer.m
#import "Computer.h"
@implementation Computer
@synthesize name;
-(void) calculate{
    NSLog(@"i can calculate");
}
@end

//  MacBook.h
#import "Computer.h"
@interface MacBook : Computer
@end

//  MacBook.m
#import "MacBook.h"
@implementation MacBook
@end

//main.m
int main(int argc, char *argv[])
{
    @autoreleasepool
    {
        MacBook *macBook = [[MacBook alloc] init];
        macBook.name = @"mac";
        [macBook calculate];
    }
}
```



### 多态

封装、继承和多态是面向对象编程语言的三大特性，OC 的多态是不同对象对同一消息的不同响应方式，实际过程主要分为三种：继承、重写、指向子类的指针指向父类。可以看出跟 Java 的多态类似，理解起来应该比较容易，注意是没有方法重载的，在 OC 中不允许。

### 快速枚举

比起利用 NSEnumerator 对象或在集合中依次枚举，Objective-C 2.0 提供了快速枚举的语法。快速枚举可以比标准枚举产生更有效的代码，由于枚举所调用的方法被使用 NSFastEnumeration 协议提供的指针算术运算所代替了。在 Objective-C 2.0 中，以下循环的功能是相等的，但性能特性不同。

```objective-c
// 使用NSEnumerator
NSEnumerator *enumerator = [thePeople objectEnumerator];
Person *p;
while ( (p = [enumerator nextObject]) != nil ) {
    NSLog(@"%@ is %i years old.", [p name], [p age]);
}
// 使用依次枚举
for ( int i = 0; i < [thePeople count]; i++ ) {
    Person *p = [thePeople objectAtIndex:i];
    NSLog(@"%@ is %i years old.", [p name], [p age]);
}
// 使用快速枚举
for (Person *p in thePeople) {
    NSLog(@"%@ is %i years old.", [p name], [p age]);
}
```



### 协议（Protocol）

协议是一组没有实现的方法列表，任何的类均可采纳协议并具体实现这组方法。协议类似于 Java 与 C# 语言中的"接口"。在 Objective-C 中有两种定义协议的方式：由编译器保证的"正式协议"，以及为特定目的设定的"非正式协议"。协议经常应用于Cocoa中的委托及事件触发。

**非正式协议** 为一个可以选择性实现的一系列方法列表。非正式协议虽名为协议，但实际上是挂于NSObject上的未实现分类（Unimplemented Category）的一种称谓，Objetive-C语言机制上并没有非正式协议这种东西，OSX 10.6 版本之后由于引入 @optional 关键字，使得正式协议已具备同样的能力，所以非正式协议已经被废弃不再使用。

**正式协议 ** 类似于Java中的"接口"，它是一系列方法的列表，任何类都可以声明自身实现了某个协议。在Objective-C 2.0 之前，一个类必须实现它声明匹配的协议中的所有方法，否则编译器会报告错误，表明这个类没有实现它声明匹配的协议中的全部方法。Objective-C 2.0 版本允许标记协议中某些方法为可选的（Optional），这样编译器就不会强制实现这些可选的方法。

但，Objective-C 中协议的概念与 Java 中接口的概念并不完全相同，即一个类可以在不声明它匹配某个协议的情况下，实现这个协议所包含的方法，也即实质上匹配这个协议，而这种差别对外部代码而言是不可见的。正式协议的声明不提供实现，它只是简单地表明匹配该协议的类实现了该协议的方法，保证调用端可以安全调用方法。（啥意思，没懂？？？？）

协议以关键字 @protocol 作为区块起始，@end 结束，中间为方法列表。

```objective-c
@protocol Locking
- (void)lock;
- (void)unlock;
@end
```

以上是一个协议的例子，多线程编程中经常要确保一份共享资源同时只有一个线程可以使用，会在使用前给该资源挂上锁 ，以上即为一个表明有"锁"的概念的协议，协议中有两个方法，只有名称但尚未实现。下面的SomeClass宣称他采纳了Locking协议：

```objective-c
@interface SomeClass : SomeSuperClass <Locking>
@end
```

一旦SomeClass表明他采纳了Locking协议，SomeClass就有义务实现Locking协议中的两个方法。由于SomeClass已经确实遵从了Locking协议，故调用端可以安全的发送lock或unlock消息给SomeClass实体变量，不需担心他没有办法回应消息。

```objective-c
@implementation SomeClass
- (void)lock {
  // 实现lock方法...
}
- (void)unlock {
  // 实现unlock方法...
}
@end
```

插件是另一个使用抽象定义的例子，可以在不关心插件的实现的情况下定义其希望的行为。

### 动态类型

类似于 Smalltalk，Objective-C 具备动态类型：即消息可以发送给任何对象实体，无论该对象实体的公开接口中有没有对应的方法。对比于 C++ 这种静态类型的语言，编译器会挡下对（void* ）指针调用方法的行为。但在 Objective-C 中，你可以对 id 发送任何消息（id 很像 void*，但是被严格限制只能使用在对象上），编译器仅会发出"该对象可能无法回应消息"的警告，程序可以通过编译，而实际发生的事则取决于运行期该对象的真正形态，若该对象的确可以回应消息，则依旧运行对应的方法。

一个对象收到消息之后，他有三种处理消息的可能。第一是回应该消息并运行方法；若无法回应，则可以转发消息给其他对象；若以上两者均无，就要处理无法回应而抛出的例外。只要进行三者之其一，该消息就算完成任务而被丢弃。若对"nil"（空对象指针）发送消息，该消息通常会被忽略，取决于编译器选项可能会抛出例外。

虽然 Objective- C具备动态类型的能力，但编译期的静态类型检查依旧可以应用到变量上。以下三种声明在运行时效力是完全相同的，但是三种声明提供了一个比一种声明更明显的类型信息，附加的类型信息让编译器在编译时可以检查变量类型，并对类型不符的变量提出警告。下面三个方法，差异仅在于参数的形态：

```objective-c
- setMyValue:(id) foo; // id形态表示参数"foo"可以是任何类的实例。
- setMyValue:(id <aProtocol>) foo; // id<aProtocol>表示"foo"可以是任何类的实例，但必须采纳"aProtocol"协议。
- setMyValue:(NSNumber*) foo; // 该声明表示"foo"必须是"NSNumber"的实例。
```

动态类型是一种强大的特性。在缺少泛型的静态类型语言（如 Java 5 以前的版本）中实现容器类时，程序员需要写一种针对通用类型对象的容器类，然后在通用类型和实际类型中不停的强制类型转换。无论如何，类型转换会破坏静态类型，例如写入一个"整数"而将其读取为"字符串"会产生运行时错误。这样的问题被泛型解决，但容器类需要其内容对象的类型一致，而对于动态类型语言则完全没有这方面的问题。

### 转发

Objective-C 允许对一个对象发送消息，不管它是否能够响应之。除了响应或丢弃消息以外，对象也可以将消息转发到可以响应该消息的对象。转发可以用于简化特定的设计模式，例如观测器模式或代理模式。如下，Objective-C 运行时在 Object 中定义了一对方法：

```objective-c
// 转发方法：（不知下面方法是否能实践）
- (retval_t) forward:(SEL) sel :(arglist_t) args; // with GCC
- (id) forward:(SEL) sel :(marg_list) args; // with NeXT/Apple systems
// 响应方法：
- (retval_t) performv:(SEL) sel :(arglist_t) args;  // with GCC
- (id) performv:(SEL) sel :(marg_list) args; // with NeXT/Apple systems
```

希望实现转发的对象只需用新的方法覆盖以上方法来定义其转发行为。无需重写响应方法 performv::，由于该方法只是单纯的对响应对象发送消息并传递参数。其中，SEL 类型是 Objective-C 中消息的类型。

```objective-c
#import <Foundation/Foundation.h>
@interface Person : NSObject
@end

@interface Father : NSObject
- (void)speak:(NSString *)aString;
@end

@implementation Person
- (id)forwardingTargetForSelector:(SEL)aSelector {
    return [[Father alloc] init];
}
@end

@implementation Father
- (void)speak:(NSString *)aString {
    NSLog(@"%@", aString);
}
@end

int main(int argc, const char *argv[]) {
    @autoreleasepool {
        id person = [[Person alloc] init];
        [person performSelector: @selector(speak:) withObject:@"hello"];  // hello
    }
    return 0;
}
// 输出：    hello
```



### 类别 (Category)

在 Objective-C 的设计中，一个主要的考虑即为大型代码框架的维护。结构化编程的经验显示，改进代码的一种主要方法即为将其分解为更小的片段。Objective-C借用并扩展了 Smalltalk 实现中的"分类"概念，用以帮助达到分解代码的目的。

一个分类可以将方法的实现分解进一系列分离的文件。程序员可以将一组相关的方法放进一个分类，使程序更具可读性。进一步的，分类中的方法是在运行时被加入类中的，这一特性允许程序员向现存的类中增加方法，而无需持有原有的代码，或是重新编译原有的类。在运行时，分类中的方法与类原有的方法并无区别，其代码可以访问包括私有类成员变量在内的所有成员变量。

若分类声明了与类中原有方法同名的函数，则分类中的方法会被调用。因此分类不仅可以增加类的方法，也可以代替原有的方法。这个特性可以用于修正原有代码中的错误，更可以从根本上改变程序中原有类的行为。若两个分类中的方法同名，则被调用的方法是不可预测的。

在 Xcode 中给某个类 CPerson 创建多个分类：（创建文件时 File Type 选择 Category）

```objective-c
// CPerson+Study.h
@interface CPerson (Study)
- (void)code;
- (void)read;
@end
// CPerson+Study.m
@implementation CPerson (Study)
- (void)code {
    NSLog(@"敲代码");
}
- (void)read {
    NSLog(@"读书");
}
@end
// CPerson+Live.h
@interface CPerson (Live)
- (void)eat;
- (void)drink;
@end
// CPerson+Live.m
@implementation CPerson (Live)
- (void)eat {
    NSLog(@"吃饭");
}
- (void)drink {
    NSLog(@"喝水");
}
@end
// 主函数
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        CPerson *ps = [[CPerson alloc] init];
        // 生存相关方法
        [ps eat];
        // 学习相关方法
        [ps code];
    }
    return 0;
}
```

注意：

1. 分类中只能增加方法，不能增加属性,否则会编译报错。
2. 分类中可以写 @property，但是只会生成 getter 和 setter 的声明，不会生成 getter 和 setter 的实现。编译可通过，但调用会崩溃。
3. 在分类的方法中不能直接访问本类的私有属性，但是可以用 setter、getter 方法访问。
4. 当分类中有和本类重名的方法，优先调用分类的方法，即使没有引入分类的头文件。如果多个分类中都有相同的方法，优先调用最后编译的方法。



### 垃圾收集

Objective-C 2.0 提供了一个可选的垃圾收集器。在向后兼容模式中，Objective-C 运行时会将引用计数操作，例如"retain"与"release"变为无操作。当垃圾收集启用时，所有的对象都是收集器的工作对象。普通的C指针可以以"__ strong"修饰，标记指针指向的对象仍在使用中。被标记为"__weak"的指针不被计入收集器的计数中，并在对象被回收时改写为"nil"。iOS 上的 Objective-C 2.0 实现中不包含垃圾收集器。垃圾收集器运行在一个低优先级的后台线程中，并可以在用户动作时暂停，从而保持良好的用户体验。

NSObject协议声明了Retain、release和autorelease方法用于操作计数器，分别是递增、递减、自动释放操作，所有的对象都是收集器的工作对象。OC中引入自动引用计数（ARC），内存管理交由编译器决定。

### 异常处理

OC 的异常处理极其类似 Java 中的，包括4个指示符，分别是 @try、@catch、@throw、@finally。可能存在异常的代码写在 @try 块，异常处理逻辑写在@catch，@finally 块的代码总是要执行的，@throw 作用是抛出异常。

### 单例模式

一种实现： 单例顾名思义就是说一个类的实例只能有一个，在 java、C++ 这类语言中，可以通过将构造函数私有化来避免对象的重复创建，但是 objective-c 却不能够这样做，我们需要通过其他机制来达到这个目的。为了确保对象的唯一性，也需要封锁用户通过 alloc 和 init 以及 copy 来构造对象这条道路。

创建对象的步骤分为申请内存(alloc)、初始化(init)这两个步骤，我们要确保对象的唯一性，因此在第一步这个阶段我们就要拦截它。当我们调用 alloc 方法时，oc内部会调用 allocWithZone 这个方法来申请内存，我们覆写这个方法，然后在这个方法中调用 shareInstance 方法返回单例对象，这样就可以达到我们的目的。拷贝对象也是同样的原理，覆写 copyWithZone 方法，然后在这个方法中调用 shareInstance 方法返回单例对象。

```objective-c
//  Singleton.h    不一定完全正确
#import <Foundation/Foundation.h>
@interface Singleton : NSObject
+(instancetype) shareInstance ;
@end
//  Singleton.m
#import "Singleton.h"
@implementation Singleton
static Singleton* _instance = nil;
 
+(instancetype) shareInstance {
    static dispatch_once_t onceToken ;
    dispatch_once(&onceToken, ^{
        _instance = [[super allocWithZone:NULL] init] ;
    }) ;
    return _instance ;
}
+(id) allocWithZone:(struct _NSZone *)zone {
    return [Singleton shareInstance] ;
}
-(id) copyWithZone:(struct _NSZone *)zone {
    return [Singleton shareInstance] ;
}
@end
// main
#import <Foundation/Foundation.h>
#import "Singleton.h"
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        
        Singleton* obj1 = [Singleton shareInstance] ;
        NSLog(@"obj1 = %@.", obj1) ;
        Singleton* obj2 = [Singleton shareInstance] ;
        NSLog(@"obj2 = %@.", obj2) ;
        Singleton* obj3 = [[Singleton alloc] init] ;
        NSLog(@"obj3 = %@.", obj3) ;        
        Singleton* obj4 = [[Singleton alloc] init] ;
        NSLog(@"obj4 = %@.", [obj4 copy]) ;
    }
    return 0;
}
```



### block

block 实际上就是 Objective-C 语言对闭包的实现。类似 Java 中的 Lambda 表达式。

[block的数据结构](https://blog.csdn.net/wg4oma28/article/details/123366717) ：

[block基本使用](https://blog.csdn.net/weixin_43899582/article/details/122934784?spm=1001.2014.3001.5502) ：block 又称之为代码段，是一个可以存储代码的数据类型。

[从基础知识引出闭包的逻辑](https://windzen.blog.csdn.net/article/details/42638489?spm=1001.2014.3001.5502)  ：由于 block 数据类型的语法会降低整个代码的阅读性，所以常使用 typedef 来定义 block 类型。

[闭包的作用](https://blog.csdn.net/weixin_56266471/article/details/125225998) ：通过函数作用域和内存回收机制的铺垫引出闭包：在一个函数里边再定义一个函数。这个内部函数一直保持有对外部函数中作用域的访问，从而使外部函数作用域及其局部变量始终保存在内存中不会被回收。（通过一系列方法，将函数内部的变量(局部变量)转化为全局变量）

```objective-c
// 语法   // 返回值类型 (^block变量名称)(参数列表);
// 例子1：一个无返回值，无参数的block
void (^myBlock)();
// 例子2：有返回值，无参数的block
int (^myBlock)();
// 例子3：有返回值，有参数的block
int (^myBlock)(int num1,int num2);
```

简写规则：

1. 如果写的代码段没有返回值，那么**代码段**的返回值可以省略
2. 如果写的代码段没有参数，那么**代码段**的小括号可以省略
3. 结合1、2，既没有返回值，也没有参数的block，则可以将返回值与参数列表的小括号全部省略掉
4. **声明** block 变量的时候，如果有指定参数，可以只写参数的类型而不写参数的名称
5. block 的返回值：无论代码段是否有返回值，在写代码段的时候都可以省略，系统会自动的确认返回值的类型。（如果代码段中没有返回任何数据，系统会认为这个代码段没有返回值；如果代码中有返回数据，返回的数据是什么类型，那么系统会认为这个代码段的返回值就是什么类型）

```objective-c
// 1 如果写的代码段没有返回值，那么代码段的返回值可以省略
void (^myBlock)(int num) = ^void(int num){
    ......
};
void (^myBlock)(int num) = ^(int num){
    ......
};
// 2 如果写的代码段没有参数，那么代码段的小括号可以省略
int (^myBlock)() = ^int(){
    ......
};
int (^myBlock)() = ^int{
    ......
};
// 3 结合1、2，既没有返回值，也没有参数的block，则可以将返回值与参数列表的小括号全部省略掉
void (^myBlock)() = ^void(){
    ......
};
void (^myBlock)() = ^{
    ......
};
// 4 声明 block 变量的时候，如果有指定参数，可以只写参数的类型而不写参数的名称
int (^myBlock)(int num) = ^int(int num) {
    ......
};
int (^myBlock)(int) = ^int(int num) {
    ......
};
// 5 block 的返回值  // 举个例子，下面的代码块返回值类型为int
int (^myBlock)() = ^ {
    return 1;
};
```

typedef 定义 block：

```objective-c
// 语法   typedef 返回值类型 (^block名称)(参数列表);
typedef int (^myBlock)(int num1, int num2);
```

block 访问外部变量：

1. 在 block 内部可以读取定义在外部的变量的值，包括外部的局部变量和全局变量。
2. 在 block 内部可以修改定义在外部全局变量的值，但是不可以修改定义在外部的局部变量。
3. 如果想在 block 内部修改定义在外部的局部变量，需要在外部变量的定义前加上关键字 __block。

block 作为方法参数：的直观作用是被调用的方法可以按照调用者的意愿完成某些逻辑

```objective-c
// 用于存储排序方法的代码段
typedef NSArray*(^sortBlock)(NSArray *);

int main(){
    // 字符串数组
    NSArray *arr = @[@"Korean",@"China",@"America"];
    // 小红的方法
    sortBlock xiaohongBlock = ^NSArray*(NSArray *){
        return @[@"America",@"China",@"Korean"];
    };
    // 小明的方法
    sortBlock xiaomingBlock = ^NSArray*(NSArray *){
        return @[@"China",@"Korean",@"America"];
    };
    
    return 0;
}
// 排序方法
- (void)showWithArr:(NSArray *)arr withMySortBlock:(sortBlock) myBlock{
    NSInteger nLen = [arr count];
    NSArray *afterSortArr = myBlock(arr);
    for (int i = 0; i < nLen ;i++) {
        NSLog(@"%@",afterSortArr[i]);
    }
}
```

block 作为方法的返回值

```objective-c
int main(){
    void(^myBlock)(void) = [self show];
    myBlock();
    
    return 0;
}

-(void(^)(void))show{
    return ^void(){
        NSLog(@"block 作为函数返回值");
    };
}
```



### SEL的原理及使用

SEL：全称为 selector，本质是一个数据类型。SEL的对象是用来存储方法的。

如何将方法存储在类对象中：

1. 先创建一个SEL对象
2. 将方法的信息存储在这个SEL对象中
3. 再讲这个SEL对象作为类对象的属性

调用方法的本质：

1. 当我们调用show方法时，先拿到存储show方法的SEL对象。
2. 以消息的形式发送给ps对象。
3. ps收到消息后，根据对象的isa指针找到对应存储类。
4. 找到这个类后，在这个类中去寻找是否有和传入的SEL数据相匹配的方法。如果有，则执行方法。如果没有，再去父类寻找，直到找到NSobject为止。

```objective-c
Person *ps = [[Person alloc] init];
[ps show];
```



### 内存管理

<span id="jump">跳转到的地方</span>                 <a id="table1">Table - 1</a>    #要跳转的位置,id = 链接位置

OC 中对象内存管理： OC 中通过引用计数来管理对象的生命周期。

```objective-c
- (instancetype)retain OBJC_ARC_UNAVAILABLE;  //引用加1
- (oneway void)release OBJC_ARC_UNAVAILABLE; //引用减1
- (instancetype)autorelease OBJC_ARC_UNAVAILABLE; //自动释放对象
- (NSUInteger)retainCount OBJC_ARC_UNAVAILABLE; //返回当前的引用技术
```

当对象 B 拥有对象 A 时，设置对象 A 时，最好掉用 Retain 提升引用计数，在 dealloc 方法里面减少引用技术。



多个对象间的内存管理：类中的变量为对象时，赋值可用 call retain 方法，用于管理引用（利用 retainCount 方法验证引用数量）

Dealloc ： 当类中包含有其它对象时，就需要通过重写 dealloc 函数 dealloc 这些对象。

```objective-c
@interface Book : NSObject
@property int page;
@end

@implementation Book
@end

@interface Person : NSObject
@property (retain) Book *book;
@end

@implementation Person
- (void)dealloc {
	[_book release];
	[super dealloc];
}
@end

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        Person *p = [[Person alloc] init];
        int c = (int)[p retainCount];
        [p release];
        p = nil; // 对象内存被释放后，将对象设置为nil，防止野指针错误。对象不能再用。
    }
}
```



## UIKit

### 基础控件学习

转场：navigationController tabBarController page

view：button tableview scrollView CollectionView label image textField

简单动画



控件组合





# 实战培训

## 前端基础

### HTML

超文本标记语言（英语：Hyper Text Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。HTML 运行在浏览器上，由浏览器来解析。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
 
<h1>我的第一个标题</h1>
 
<p>我的第一个段落。</p>
 
</body>
</html>
```

实例解析：

- `<!DOCTYPE html>`  声明为 HTML5 文档
- `<html>` 元素是 HTML 页面的根元素
- `<head>` 元素包含了文档的元（meta）数据，如 `<meta charset="utf-8">` 定义网页编码格式为 **utf-8**。
- `<title>` 元素描述了文档的标题
- `<body>` 元素包含了可见的页面内容
- `<h1>` 元素定义一个大标题
- `<p>` 元素定义一个段落

作为一种标记语言，HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由*尖括号*包围的关键词，比如 `<html>`
- HTML 标签通常是*成对出现*的，比如` <html>` 和 `</html>`
- 标签对中的第一个标签是*开始标签*，第二个标签是*结束标签*
- 开始和结束标签也被称为*开放标签*和*闭合标签*

HTML 的诸多标签可以在 [HTML 参考手册](https://www.runoob.com/tags/html-reference.html) 中查找并使用。

#### html 元素

HTML 元素以**开始标签**起始，以**结束标签**终止。元素的内容是开始标签与结束标签之间的内容。大多数 HTML 元素可拥有**属性**。

某些 HTML 元素具有空内容（empty content），空元素在开始标签中进行关闭（以开始标签的结束而结束）。在开始标签中添加斜杠是关闭空元素的正确方法。

```html
<p>这是第一个段落。</p>
<br />
```

#### html 属性

html 属性可以在元素中添加**附加信息**；一般描述于**开始标签**；总是以名称/值对的形式出现，比如：name="value"。

#### HTML  < head>  元素

在`<head>` 元素包含了所有的头部标签元素。在 `<head>`元素中你可以插入脚本（scripts）, 样式文件（CSS），及各种meta信息。

可以添加在头部区域的元素标签为: `<title>, <style>, <meta>, <link>, <script>, <noscript> 和 <base>`。

#### HTML 样式- CSS

CSS 是在 HTML 4 开始使用的,是为了更好的渲染HTML元素而引入的.

CSS 可以通过以下方式添加到HTML中:

- 内联样式- 在HTML元素中使用"style" **属性**
- 内部样式表 -在HTML文档头部 `<head>` 区域使用`<style>` **元素** 来包含CSS
- 外部引用 - 使用外部 CSS **文件**

最好的方式是通过外部引用CSS文件。

```html
<p style="color:blue;margin-left:20px;">内联样式</p>

<head>
<style type="text/css">
body {background-color:yellow;}
p {color:blue;}
</style>
</head>

<head>
<link rel="stylesheet" type="text/css" href="标签路径">
</head>

<style>
@import url("标签路径")
</style>
```

link 和 import之间的区别?

- **差别 1：** 本质的差别：**link** 属于 XHTML 标签，而 **@import** 完全是 CSS 提供的一种方式。
- **差别 2：** **加载顺序的差别：** 当一个页面被加载的时候（就是被浏览者浏览的时候) ，link 引用的 CSS 会同时被加载，而 **@import** 引用的 CSS 会等到页面全部被下载完再被加载。所以有时候浏览 **@import** 加载 CSS 的页面时开始会没有样式(就是闪烁)，网速慢的时候还挺明显。
- **差别 3：** **兼容性的差别:** **@import** 是 CSS2.1 提出的，所以老的浏览器不支持，**@import** 只有在 IE5 以上的才能识别，而 **link** 标签无此问题。
- **差别 4：** 使用 dom(document object model文档对象模型 )控制样式时的差别：当使用 javascript 控制 dom 去改变样式的时候，只能使用 link 标签，因为**@import** 不是 dom 可以控制的。

#### HTML 区块

大多数 HTML 元素被定义为**块级元素**或**内联元素**。块级元素在浏览器显示时，通常会以新行来开始（和结束），例如： `<h1>, <p>, <ul>, <table>`；内联元素在显示时通常不会以新行开始，例如：` <b>, <td>, <a>, <img>`。

HTML `<div>` 元素是块级元素，它可用于组合其他 HTML 元素的容器。它`<div>` 元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示折行。如果与 CSS 一同使用，`<div>` 元素可用于对大的内容块设置样式属性。

> 另外，`<div>` 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。使用 `<table>` 元素进行文档布局不是表格的正确用法。`<table>` 元素的作用是显示表格化的数据。

HTML `<span>` 元素是内联元素，可用作文本的容器。`<span>` 元素也没有特定的含义。当与 CSS 一同使用时，`<span>` 元素可用于为部分文本设置样式属性。



### JavaScript

JavaScript 是 Web 的编程语言。JavaScript 是一个脚本语言。

HTML 中的 JavaScript 脚本代码必须位于 `<script>` 与 `</script>` 标签之间。JavaScript 脚本代码可被放置在 HTML 页面的 `<body>` 和 `<head>` 部分中，或者保存到外部文件(.js)中。

```html
<script src="myScript.js"></script>
```

#### JavaScript 显示数据

JavaScript 不提供任何内建的打印或显示函数。

JavaScript 可以通过不同的方式来输出数据：

- 使用 **window.alert()** 弹出警告框。
- 使用 **document.write()** 方法将内容写到 HTML 文档中。
- 使用 **innerHTML** 写入到 HTML 元素。
- 使用 **console.log()** 写入到浏览器的控制台。

如需从 JavaScript 访问某个 HTML 元素，可以使用 document.getElementById(*id*) 方法。使用 "id" 属性来标识 HTML 元素，并 innerHTML 来获取或插入元素内容：

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>
<p id="demo">我的第一个段落</p>

<script>
document.getElementById("demo").innerHTML = "段落已修改。";
</script>

</body>
</html>
```

#### JavaScript 语法

**字面量**：在 js 中，一般固定值称为字面量。包括：

- 数字（Number）字面量，可以是整数或者是小数，或者是科学计数(e)。
- 字符串（String）字面量，可以使用单引号或双引号
- 表达式字面量，用于计算。
- 数组（Array）字面量，定义一个数组。
- 对象（Object）字面量，定义一个对象。
- 函数（Function）字面量，定义一个函数。

**变量**：JavaScript 使用关键字 **var** 来定义变量， 使用等号来为变量赋值。声明但未赋值的变量，它的值将是 `undefined`。

> 变量是一个**名称**。字面量是一个**值**。JavaScript 对大小写是敏感的。
>
> let 声明了块作用域（*Block Scope*）变；const 声明常量（它没有定义常量值。它定义了对值的常量引用）。这两类都拥有块作用域。

```js
typeof null                   // object  //在 JavaScript 中，null 的数据类型是对象。
typeof undefined              // undefined
// NULL 与 undefined 是不同的。清空对象时：
var person = null;           // 值是 null，但是类型仍然是对象。
var person = undefined;      // 值是 undefined，类型是 undefined。
```

**JavaScript 标识符**：用于命名变量（以及关键词、函数和标签）。首字符必须是字母、下划线（-）或美元符号（$）。连串的字符可以是字母、数字、下划线或美元符号。

**JavaScript 操作符**：= + - * /     == != < > 

**JavaScript 语句**：在 HTML 中，JavaScript 语句用于向浏览器发出命令。语句是用分号分隔（在 JavaScript 中，用分号来结束语句是可选的）。

```js
function functionName(a, b) {
    return a * b;                                // 返回 a 乘以 b 的结果
}
```

#### JavaScript 对象

对象访问与对象方法的使用：

```js
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue",
             fullName : function() {return this.firstName + " " + this.lastName;}
             };
person.lastName;  // 访问对象属性方式1
person["lastName"];  // 访问对象属性方式2
name = person.fullName();  // 添加()，调用该方法。
method = person.fullName;  // 不加()，它将作为一个定义函数的字符串返回。
```

#### JavaScript 函数

全局变量、局部变量。



### CSS

**CSS** (Cascading Style Sheets，层叠样式表），是一种用来为结构化文档（如 HTML 文档或 XML 应用）添加样式（字体、间距和颜色等）的计算机语言，**CSS** 文件扩展名为 **.css**

#### CSS 语法

CSS 规则由两个主要的部分构成：选择器，以及一条或多条声明:

```css
p {color:red;text-align:center;}
```

选择器通常是您需要改变样式的 HTML 元素。每条声明由一个属性和一个值组成，属性和值被冒号分开。

CSS声明总是以分号 `;` 结束，声明总以大括号 `{}` 括起来。

##### id 选择器

id 选择器可以为标有特定 id 的 HTML 元素指定特定的样式。HTML元素以id属性来设置id选择器,CSS 中 id 选择器以 "#" 来定义。以下的样式规则应用于元素属性 id="para1":

```css
#para1 {
    text-align:center;
    color:red;
}
```

> 注：ID属性不要以数字开头，数字开头的ID在 Mozilla/Firefox 浏览器中不起作用。

##### class 选择器

class 选择器用于描述一组元素的样式，class 选择器有别于id选择器，class可以在多个元素中使用。以下的样式规则，所有拥有 center 类的 HTML 元素均为居中。

class 选择器在 HTML 中以 class 属性表示, 在 CSS 中，类选择器以一个点 `.` 号显示：

```css
.center {text-align:center;}
```

你也可以指定特定的 HTML 元素使用 class。在以下实例中, 所有的 p 元素使用 class="center" 让该元素的文本居中:

```css
p.center {text-align:center;}
```

#### 多重样式优先级

样式表允许以多种方式规定样式信息。 优先级：内联样式 > 内部样式表 > 外部样式表 > 浏览器样式表

css 7 种选择器： id 选择器、类选择器、伪类选择器、 属性选择器、 伪元素选择器、 通配选择器、 标签选择器

CSS 优先规则：内联样式 > id 选择器 > 类选择器 = 伪类选择器 = 属性选择器 > 标签选择器 = 伪元素选择器

**!important 规则例外** ，当 !important 规则被应用在一个样式声明中时,该样式声明会覆盖CSS中任何其他的声明, 无论它处在声明列表中的哪里。

#### CSS 嵌套选择器

它可能适用于选择器内部的选择器的样式。在下面的例子设置了四个样式：

- **p{ }**: 为所有 **p** 元素指定一个样式。
- **.marked{ }**: 为所有 **class="marked"** 的元素指定一个样式。
- **.marked p{ }**: 为所有 **class="marked"** 元素内的 **p** 元素指定一个样式。
- **p.marked{ }**: 为所有 **class="marked"** 的 **p** 元素指定一个样式。



### less

less是一种 css 预编译处理语言，能使用变量，函数等功能，比 css 具有更强大的功能。Less 仅对 CSS 语言增加了少许方便的扩展，这就是 Less 如此易学的原因之一。

参考： [Less快速入门](https://less.bootcss.com/) 、[随便搜的一篇文章](https://www.jianshu.com/p/39bff2b06db9)

#### 变量

@变量名:变量值;

```less
@width: 10px;
@height: @width + 10px;  // 变量可运算
#header {
  width: @width;
  height: @height;
}
```



### VUE

Vue 是一款用于构建用户界面的 JavaScript 框架。它基于标准 HTML、CSS 和 JavaScript 构建，并提供了一套声明式的、组件化的编程模型。

VUE是一套**前端框架**，免除了原生JavaScript中的**DOM操作**，简化书写。VUE基于**MVVM**（Model-View_ViewModel）思想，实现**数据双向绑定**。

#### 单文件组件

**单文件组件** (也被称为 `*.vue` 文件，英文 Single-File Components，缩写为 **SFC**)。Vue 的单文件组件会将一个组件的逻辑 (JavaScript)，模板 (HTML) 和样式 (CSS) 封装在同一个文件里。

```vue
<script>
export default {
  data() {
    return {
      count: 0
    }
  }
}
</script>

<template>
  <button @click="count++">Count is: {{ count }}</button>
</template>

<style scoped>
button {
  font-weight: bold;
}
</style>
```



### 其他知识

#### MVVM 和 MVC 有什么区别？

MVC：MVC是一种设计模式：

- M（Model）：模型层。是应用程序中用于处理应用程序数据逻辑的部分，模型对象负责在数据库中存取数据；
- V（View）：视图层。是应用程序中处理数据显示的部分，视图是依据模型数据创建的；
- C（Controller）：控制层。是应用程序中处理用户交互的部分，控制器接受用户的输入并调用模型和视图去完成用户的需求，控制器本身不输出任何东西和做任何处理。它只是接收请求并决定调用哪个模型构件去处理请求，然后再确定用哪个视图来显示返回的数据。

 MVVM：

- vue框架中MVVM的M就是后端的数据，V就是节点树，VM就是new出来的那个Vue({})对象
- M（Model）：模型层。就是业务逻辑相关的数据对象，通常从数据库映射而来，我们可以说是与数据库对应的model。
- V（View）：视图层。就是展现出来的用户界面。
- VM（ViewModel）：视图模型层。连接view和model的桥梁。因为，Model层中的数据往往是不能直接跟View中的控件一一对应上的，所以，需要再定义一个数据对象专门对应view上的控件。而ViewModel的职责就是把model对象封装成可以显示和接受输入的界面数据对象。

MVVM与MVC的最大区别就是：它实现了View和Model的自动同步，也就是当Model的数据改变时，我们不用再自己手动操作Dom元素，来改变View的显示，而是改变数据后该数据对应View层显示会自动改变。（[参考自网络](https://blog.csdn.net/weixin_48841931/article/details/126219434)）



## 后端基础

### Java 基础

接口是什么？抽象类、内部类、正则表达式、包、泛型（常用吗）、关键字（super/synchronized）、注解、反射、

spring cloud：是基于SpringBoot的一整套实现微服务的框架

#### Java 基础语法

```java
import java.io.*;  // 命令编译器载入 java_installation/java/io 路径下的所有类
public class HelloWorld {  // 它将输出字符串 Hello World
    public static void main(String[] args) {
        System.out.println("Hello World"); // 输出 Hello World
        final double PI = 3.1415927;  // Java 常量
    }
}
```

一个 Java 程序，应注意以下几点：

- **大小写敏感**：Java 是大小写敏感的，这就意味着标识符 Hello 与 hello 是不同的。
- **类名**：对于所有的类来说，类名的首字母应该大写。如果类名由若干单词组成，那么每个单词的首字母应该大写，例如 **MyFirstJavaClass** 。
- **方法名**：所有的方法名都应该以小写字母开头。如果方法名含有若干单词，则后面的每个单词首字母大写。
- **源文件名**：源文件名必须和类名相同。当保存文件的时候，你应该使用类名作为文件名保存（切记 Java 是大小写敏感的），文件名的后缀为 **.java**。（如果文件名和类名不相同则会导致编译错误）。
- **主方法入口**：所有的 Java 程序由 **public static void main(String[] args)** 方法开始执行。

Java可以使用 Java 修饰符来修饰类中方法和属性。主要有两类修饰符：

- **访问控制修饰符** : default, public , protected, private
- **非访问控制修饰符** : final, abstract, static, synchronized

一个类可以包含以下类型变量：

- **局部变量**：在方法、构造方法或者语句块中定义的变量被称为局部变量。变量声明和初始化都是在方法中，方法结束后，变量就会自动销毁。
- **成员变量**：成员变量是定义在类中，方法体之外的变量。这种变量在创建对象的时候实例化。成员变量可以被类中方法、构造方法和特定类的语句块访问。
- **类变量**：类变量也声明在类中，方法体之外，但必须声明为 **static** 类型。

创建对象需要以下三步：

- **声明**：声明一个对象，包括对象名称和对象类型。
- **实例化**：使用关键字 new 来创建一个对象。
- **初始化**：使用 new 创建对象时，会调用构造方法初始化对象。

源文件的声明规则。当在一个源文件中定义多个类，并且还有 import 语句和 package 语句时，要特别注意这些规则：

- 一个源文件中只能有一个 public 类
- 一个源文件可以有多个非 public 类
- 源文件的名称应该和 public 类的类名保持一致。例如：源文件中 public 类的类名是 Employee，那么源文件应该命名为Employee.java。
- 如果一个类定义在某个包中，那么 package 语句应该在源文件的首行。
- 如果源文件包含 import 语句，那么应该放在 package 语句和类定义之间。如果没有 package 语句，那么 import 语句应该在源文件中最前面。
- import 语句和 package 语句对源文件中定义的所有类都有效。在同一源文件中，不能给不同的类不同的包声明。

Java 包：主要用来对类和接口进行分类。当开发 Java 程序时，可能编写成百上千的类，因此很有必要对类和接口进行分类。

import 语句：就是用来提供一个合理的路径，使得编译器可以找到某个类。

#### Java  基本数据类型

**内置数据类型**：Java 语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

- byte 类型用在大型数组中节约空间，主要代替整数，因为 byte 变量占用的空间只有 int 类型的四分之一；
- Short 数据类型也可以像 byte 那样节省空间。一个short变量是int型变量所占空间的二分之一；
- 一般地整型变量默认为 int 类型；
- long 主要使用在需要比较大整数的系统上；
- float 在储存大型浮点数组的时候可节省内存空间；
- float 和 double 类型不能表示精确的值，如货币；

| 数据类型 | byte         | short             | int          | long        | float | double | boolean | char               |
| -------- | ------------ | ----------------- | ------------ | ----------- | ----- | ------ | ------- | ------------------ |
| 位数     | 8            | 16                | 32           | 64          | 32    | 64     |         | 16 位 Unicode 字符 |
| 最大值   | 127（2^7-1） | 32767（2^15 - 1） | （2^31 - 1） | （-2^63）   |       |        |         | \uffff             |
| 最小值   | -128（-2^7） | -32768（-2^15）   | （-2^31）    | （2^63 -1） |       |        |         | \u0000             |
| 默认值   | 0            | 0                 | 0            | 0L          | 0.0F  | 0.0D   | false   |                    |

**引用类型**：引用类型指向一个对象，指向对象的变量是引用变量。这些变量在声明时被指定为一个特定的类型。变量一旦声明后，类型就不能被改变了。（Java中的引用类型的变量非常类似于C/C++的指针）

- 对象、数组都是引用数据类型。
- 所有引用类型的默认值都是null。
- 一个引用变量可以用来引用任何与之兼容的类型。

**常量**：常量在程序运行时是不能被修改的。在 Java 中使用 final 关键字来修饰常量。

**自动类型转换**：转换从低级到高级：byte,short,char—> int —> long—> float —> double 

数据类型转换必须满足如下规则：

- \1. 不能对boolean类型进行类型转换。
- \2. 不能把对象类型转换成不相关类的对象。
- \3. 在把容量大的类型转换为容量小的类型时必须使用强制类型转换。
- \4. 转换过程中可能导致溢出或损失精度
- \5. 浮点数到整数的转换是通过舍弃小数得到，而不是四舍五入

强制类型转换

- 条件是转换的数据类型必须是兼容的。
- 格式：(type)value     type是要强制类型转换后的数据类型

隐含强制类型转换：整数的默认类型是 int；小数默认是 double 类型浮点型。



### 其他知识

微服务结构：微服务架构模式就是将整个Web应用组织为一系列小的Web服务。这些小的Web服务可以独立地编译及部署，并通过各自暴露的API接口相互通讯。它们彼此相互协作，作为一个整体为用户提供功能，却可以独立地进行扩展。 [微服务介绍网页](https://doocs.github.io/advanced-java/#/docs/micro-services/microservices-introduction?id=微服务) 

如何设计一个高并发系统？

- 系统拆分。将一个系统拆分为多个子系统，然后每个系统连一个数据库，这样本来就一个库，现在多个数据库，用于扛高并发。
- 缓存。大部分的高并发场景，都是**读多写少**。
- MQ。可能你还是会出现高并发写的场景。大量的写请求灌入 MQ 里，排队慢慢玩，**后边系统消费后慢慢写**，控制在 mysql 承载范围之内。考虑用 MQ 来异步写，提升并发性。（redis 是缓存，数据随时可能被 LRU 了，数据格式简单，没有事务支持。所以该用 mysql 。）
- 分库分表。如果数据库层面仍然满足不了抗高并发的要求，那么就将一个数据库拆分为多个库，然后将一个表**拆分为多个表** ，提高 sql 跑的性能。
- 读写分离。大部分时候数据库可能也是读多写少，没必要所有请求都集中在一个库上，可以搞主从架构，**主库写**入，**从库读**取，搞一个读写分离。**读流量太多**的时候，还可以**加更多的从库**。
- Elasticsearch，简称 es。es 是分布式的容，分布式天然就可以支撑高并发。一些比较简单的查询、统计类的操作，可以考虑用 es 来承载，还有一些全文搜索类的操作，也可以考虑用 es 来承载。

## 测试



