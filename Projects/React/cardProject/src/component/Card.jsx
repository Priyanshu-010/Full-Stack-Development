import React from "react";
import { Bookmark } from "lucide-react";

const Card = ({ card }) => {
  return (
    <div className="bg-white h-80 w-70 rounded-xl p-6 flex flex-col justify-between">
      {/* top */}
      <div className="flex items-start justify-between mb-6">
        <img
          src={card.brandLogo}
          className="h-10 w-10 rounded-full object-cover border border-[#dadada] p-1"
        />
        <button className="flex items-center gap-2 font-semibold text-[#8b8b8b] border-solid  border border-gray-600 px-3 py-2 bg-transparent rounded-2xl">
          Save <Bookmark size={14} />
        </button>
      </div>
      {/* centre */}
      <div className="flex-1">
        <h3 className="font-medium text-base mb-1">
          {card.companyName} 
          <span className="text-xs font-normal text-[#aeaeae] ml-1">
            {card.datePosted}
          </span>
        </h3>
        <h2 className="text-[21px] font-medium mb-2">{card.post}</h2>
        <div className="flex gap-1 mt-2.5">
          <h4 className="text-[10px] font-medium bg-[#e4e4e4] text-[#202020] px-2 py-1 rounded-[3px]">{card.tag1}</h4>
          <h4 className="text-[10px] font-medium bg-[#e4e4e4] text-[#202020] px-2 py-1 rounded-[3px]">{card.tag2}</h4>
        </div>
      </div>
      {/* bottom */}
      <div className="flex items-center justify-between border-t border-[#d7d7d7ce] pt-3.5">
        <div>
          <h3 className="text-[17px] font-medium mb-1">{card.pay}</h3>
          <p className="text-[10px] text-[#8b8b8b]">{card.location}</p>
        </div>
        <button className="bg-black text-white text-[12px] px-4 py-1.5 rounded-[5px] font-normal">Apply Now</button>
      </div>
    </div>
  );
};

export default Card;
