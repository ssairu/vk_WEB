package com.example.first_vk_app
import android.graphics.Color
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.first_vk_app.databinding.SingleItemBinding


class RvAdapter(
    private var count: Int,
) : RecyclerView.Adapter<RvAdapter.ViewHolder>() {

    // create an inner class with name ViewHolder
    // It takes a view argument, in which pass the generated class of single_item.xml
    // ie SingleItemBinding and in the RecyclerView.ViewHolder(binding.root) pass it like this
    inner class ViewHolder(val binding: SingleItemBinding) : RecyclerView.ViewHolder(binding.root)

    // inside the onCreateViewHolder inflate the view of SingleItemBinding
    // and return new ViewHolder object containing this layout
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = SingleItemBinding.inflate(LayoutInflater.from(parent.context), parent, false)

        return ViewHolder(binding)
    }

    // bind the items with each item
    // of the list languageList
    // which than will be
    // shown in recycler view
    // to keep it simple we are
    // not setting any image data to view
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        with(holder){
            with(position){
                binding.rectangleText.text = "$this"
                if (this % 2 == 1){
                    binding.rectangleText.setBackgroundColor(Color.CYAN)
                } else {
                    binding.rectangleText.setBackgroundColor(Color.RED)
                }

            }
        }
    }

    // return the size of languageList
    override fun getItemCount(): Int {
        return count
    }

    fun addRectangle() {
        count++
        notifyItemInserted(count - 1)
    }
}
