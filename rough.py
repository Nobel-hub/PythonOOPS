from oops_proj import chatbook

if __name__ == "__main__":
    c1 = chatbook()
    print(c1.id)
#Using static methods
    chatbook.set_id(100)

    c2 = chatbook()
    print(c2.id)
    c3 = chatbook()
    print(c3.id)
    # print(c._chatbook__name)
    # print(c.get_name())
    # c.set_name("Nobel")
    # print(c.get_name())