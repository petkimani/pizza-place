import streamlit as st

def main():
    # Initialize the list in session state to persist across reruns
    if 'my_list' not in st.session_state:
        st.session_state.my_list = []

    # Title
    st.title("List Manager")

    # Create columns for layout
    col1, col2 = st.columns(2)

    # Add item section
    with col1:
        st.subheader("Add Item")
        new_item = st.text_input("Enter item to add")
        if st.button("Add"):
            if new_item:
                st.session_state.my_list.append(new_item)
                st.success(f"'{new_item}' has been added to the list")
            else:
                st.warning("Please enter an item to add")

    # Remove item section
    with col2:
        st.subheader("Remove Item")
        if st.session_state.my_list:
            item_to_remove = st.selectbox("Select item to remove", st.session_state.my_list)
            if st.button("Remove"):
                st.session_state.my_list.remove(item_to_remove)
                st.success(f"'{item_to_remove}' has been removed from the list")
        else:
            st.write("No items to remove")

    # Display current list
    st.subheader("Current List")
    if st.session_state.my_list:
        for i, item in enumerate(st.session_state.my_list, 1):
            st.write(f"{i}. {item}")
    else:
        st.write("The list is empty")

    # Exit button (optional - in Streamlit, users can just close the tab)
    if st.button("Clear List"):
        st.session_state.my_list = []
        st.success("List has been cleared")

if __name__ == "__main__":
    main()
