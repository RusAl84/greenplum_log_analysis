

if __name__ == '__main__':
    from find_hot_tables import find_hot_tables
    hot_tables = find_hot_tables()
    print(hot_tables)
    print(f"\n\n\n{hot_tables[0][0]} {hot_tables[0][1]}")
