from BST import binary_search_tree

class Executive:
    def __init__(self):
        self.pokemon = binary_search_tree()
        self.clone = binary_search_tree()

    def exec(self, file_name):
        input_file = open(file_name)
        for line in input_file:
            data = line.rstrip('\n').split('\t')
            self.pokemon.add(data)
        choice = None
        count_copy = 0
        copy_choice = None
        clone = None
        while choice != '6':
            print("1. Search\n2. Add\n3. Print\n4. Remove\n5. Copy\n6. Quit")
            choice = input("Select an option:")
            if choice == '1':
                copy_choice = input('Copy or original?(1 for original, 2 for copy): ')
                poke_id = input("Input pokedex number: ")
                if copy_choice == '1':
                    self.pokemon._rec_search(int(poke_id), self.pokemon.root)
                elif copy_choice == '2':
                    self.clone._rec_search(int(poke_id), self.clone.root)
            if choice == '2':
                copy_choice = input('Copy or original?(1 for original, 2 for copy): ')
                poke_name = input("Input pokemon name: ")
                poke_jap_name = input("Input Japanese pokemon name: ")
                poke_id = input("Input pokedex number: ")
                new_poke_info = [poke_name, poke_id, poke_jap_name]
                if copy_choice == '1':
                    self.pokemon.add(new_poke_info)
                if copy_choice == '2':
                    print(clone)
                    self.clone.add(new_poke_info)
            if choice == '3':
                copy_choice = input('Copy or original?(1 for original, 2 for copy): ')
                order_choice = input("Pick traversal order(pre, in, post): ")
                if copy_choice == '1':
                    if order_choice == 'pre':
                        self.pokemon.pre_order(self.pokemon.root)
                    if order_choice == 'in':
                        self.pokemon.in_order(self.pokemon.root)
                    if order_choice == 'post':
                        self.pokemon.post_order(self.pokemon.root)
                if copy_choice == '2':
                    if order_choice == 'pre':
                        self.clone.pre_order(self.clone.root)
                    if order_choice == 'in':
                        self.clone.in_order(self.clone.root)
                    if order_choice == 'post':
                        self.clone.post_order(self.clone.root)
            if choice == '4':
                copy_choice = input('Copy or original?(1 for original, 2 for copy): ')
                poke_id = input("Input pokedex number of pokemon to remove: ")
                if copy_choice == '1':
                    self.pokemon.remove(self.pokemon.root, int(poke_id))
                if copy_choice == '2':
                    self.clone.remove(self.clone.root, int(poke_id))
            if choice == '5' and count_copy == 0:
                for line in self.pokemon.pre_order(self.pokemon.root):
                    self.clone.add(line)
                count_copy = 1
            if choice == '5' and count_copy == 1:
                print("Can only have 1 copy")