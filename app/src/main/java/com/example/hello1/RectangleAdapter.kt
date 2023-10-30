package com.example.hello1

import android.graphics.Color
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.hello1.databinding.RectangleItemBinding

class RectangleAdapter: RecyclerView.Adapter<RectangleAdapter.RectangleHolder>() {
    private var rec_counter = 3

    class RectangleHolder(item: View): RecyclerView.ViewHolder(item) {
        private val binding = RectangleItemBinding.bind(item)
        fun bind(num: Int) = with(binding.rectangleText){
            text = "$num"
            if (num % 2 == 0) {
                setBackgroundColor(Color.CYAN)
            } else {
                setBackgroundColor(Color.RED)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RectangleHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.rectangle_item, parent, false)
        return RectangleHolder(view)
    }

    override fun getItemCount(): Int {
        return rec_counter
    }

    override fun onBindViewHolder(holder: RectangleHolder, position: Int) {
        holder.bind(position)
    }

    fun addRectangle() {
        rec_counter++
        notifyDataSetChanged()
    }
}